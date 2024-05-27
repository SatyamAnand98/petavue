import pandas as pd
import re
import shutil
import subprocess
from app.gpt_comm import openAI_API_Prompt
from store.logging import configure_logger

logger = configure_logger()

def prompt_processing(prompt):
    file_path = './files/petavue_structured_data.xlsx'
    new_file_name = "./files/structured_data.xlsx"

    # Copying file_path and renaming it to structured_data.xlsx
    shutil.copy(file_path, new_file_name)

    modified_file = './files/modified_structured_data.xlsx'
    df = pd.read_excel(new_file_name)
    data = df.head(10)

    code_template = '''
def Solution(file: str) -> str:
    # Write your code here
'''

    role_prompt = f"""
    You need to write complete Python code so that I can copy and paste it in this format of code: {code_template} 
    to return the result based upon the command by the user for the data stored in xlsx file. 
    The data in file {new_file_name} is: {data.to_dict(orient='records')}. 
    NOTE:
    - If the data is manipulated, return the manipulated data and store the modified content to a new file: {modified_file}
    - If the data is not manipulated, return the original data.
    - Don't give me installation guide.
    - Give me code only, no explanation, not a single extra word.
    """

    response = openAI_API_Prompt(prompt=prompt, role_prompt=role_prompt, gpt_model="gpt-4", token=1000)

    try:
        code_string = response.split('```')[1].strip()
        code_string = code_string.lstrip('python').strip()
        code_string = code_string.lstrip('Python').strip()

        # Define the name of the file where the generated code will be saved
        generated_code_file = './files/generated_code.py'

        # Write the generated code to the file
        with open(generated_code_file, 'w') as f:
            f.write(code_string)

        # Execute the generated code file
        result = subprocess.run(['python', generated_code_file, new_file_name, modified_file], capture_output=True, text=True)

        # Check if there was an error during execution
        if result.returncode != 0:
            raise RuntimeError(f"Error in generated code execution: {result.stderr}")

        # Parse the output to get the result
        output = result.stdout.strip()

        if not output:
            # Extract the function name in code_string
            function_name = re.search(r'def\s+(\w+)\(', code_string).group(1)
            # Call the function with the file path as argument after importing the generated_code_file
            exec(f"from files.generated_code import {function_name}")
            output = eval(f"{function_name}('{new_file_name}')")

        return output

    except Exception as e:
        logger.error(f"Error in generated code: {e}")
        raise e
