import pandas as pd
import re
from app.gpt_comm import openAI_API_Prompt
from store.logging import configure_logger
import shutil

logger = configure_logger()

def prompt_processing(prompt):
    file_path = './files/petavue_structured_data.xlsx'
    new_file_name = "./files/structured_data.xlsx"

    # copying file_path and rename it structured_data.xlsx
    shutil.copy(file_path, new_file_name)

    modified_file = f'./files/modified_structured_data.xlsx'
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

    response = openAI_API_Prompt(prompt=prompt, role_prompt=role_prompt, gpt_model="gpt-4")

    try:
        code_string = response.split('```')[1].strip()
        code_string = code_string.lstrip('python').strip()
        code_string = code_string.lstrip('Python').strip()

        # Extract import statements
        import_statements = re.findall(r'^\s*(import .+|from .+ import .+)', code_string, re.MULTILINE)

        # Dynamically import the modules
        for statement in import_statements:
            try:
                exec(statement, globals())
            except Exception as e:
                logger.error(f"Failed to import module with statement '{statement}': {e}")
                raise ImportError(f"Failed to import module with statement '{statement}': {e}")

        # Remove import statements from code_string
        code_string = re.sub(r'^\s*(import .+|from .+ import .+)', '', code_string, flags=re.MULTILINE).strip()

        # Remove all print statements from the code_string
        code_string = re.sub(r'print\(.*\)', '', code_string)

        # Execute the remaining code
        local_scope = {}
        exec(code_string, globals(), local_scope)

        # Extract the function name
        # function_name_match = re.search(r'def (\w+)\(file: str\)', code_string)
        # if function_name_match:
        #     function_name = function_name_match.group(1)
        # else:
        #     raise NameError("No function found in the generated code string.")
        
        # Ensure the main function (Solution) is available in the local_scope
        if 'Solution' not in local_scope:
            raise NameError("Solution function is not defined in the executed code string.")

        function_name = "Solution"

        # Ensure the function is available in the local_scope
        if function_name in local_scope:
            generated_function = local_scope[function_name]
        else:
            raise NameError(f"{function_name} function is not defined in the executed code string.")

        # Call the generated function and get the result
        result = generated_function(new_file_name)

        # If result is a DataFrame, save it to a new file
        if isinstance(result, pd.DataFrame):
            result.to_excel(modified_file, index=False)
            return {
                "message": "Data is manipulated and stored in a new file",
                "file": modified_file
            }
        elif isinstance(result, pd.Series):
            # Convert Series to a list or dict to make it JSON serializable
            return result.to_dict()
        else:
            return result

    except Exception as e:
        logger.error(f"Error in generated code: {e}")
        raise e
