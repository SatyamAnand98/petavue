import pandas as pd
import re
from app.gpt_comm import openAI_API_Prompt
import datetime
from datetime import datetime
from store.logging import configure_logger
import click
from openpyxl.styles import PatternFill
import shutil
from openpyxl import load_workbook

logger = configure_logger()

def prompt_processing(prompt):
    click.clear()
    file_path = './files/petavue_structured_data.xlsx'
    new_file_name = "./files/structured_data.xlsx"

    # copying file_path and rename it structured_data.xlsx
    shutil.copy(file_path, new_file_name)
    

    modified_file = f'./files/modified_structured_data.xlsx'
    df = pd.read_excel(new_file_name)
    data = df.head(10)

    code = f'''
    def Solution(file: str) -> str:
        # Write your code here
    '''

    role_prompt = f"you need to write complete python so that I can copy paste in this format of code: {code} to return the result based upon the command by user for the data stored in xlsx file. The data in file {new_file_name} is: {data.to_dict(orient='records')}. If the data is manipulated, return the manipulated data and store the modified content to a new file: {modified_file}"

    response = openAI_API_Prompt(prompt=prompt, role_prompt=role_prompt ,gpt_model="gpt-4")

    try:
        code_string = response.split('```')[1]

        code_string = code_string.lstrip('python').strip()
        code_string = code_string.lstrip('Python').strip()

        # Extract import statements
        imports = re.findall(r'^\s*(import .+|from .+ import .+)', code_string, re.MULTILINE)

        # Execute import statements
        local_scope = {}
        global_scope = globals()

        for imp in imports:
            exec(imp, global_scope, local_scope)

        # Remove import statements from code_string
        code_body = re.sub(r'^\s*(import .+|from .+ import .+)', '', code_string, flags=re.MULTILINE)

        # Extract function name (assuming there's only one function defined)
        function_name_match = re.search(r'def (\w+)\(file: str\)', code_body)
        if function_name_match:
            function_name = function_name_match.group(1)
        else:
            raise NameError("No function found in the generated code string.")

        # Execute the remaining code
        exec(code_body, global_scope, local_scope)

        # Now the function should be available in local_scope
        if function_name in local_scope:
            generated_function = local_scope[function_name]
        else:
            raise NameError(f"{function_name} function is not defined in the executed code string.")

        # Call the generated function and get the result
        result = generated_function(new_file_name)

        return result
    except Exception as e:
        logger.error(f"Error in generated code: {e}")
        return {
            "error": "Oops!! Something wrong happened! Please try again"
        }
