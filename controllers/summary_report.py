import pandas as pd
import re
from app.gpt_comm import openAI_API_Prompt

def report():
    file_path = './files/petavue_structured_data.xlsx'
    df = pd.read_excel(file_path)

    numerical_columns = df.select_dtypes(include=['number']).columns


    for col in numerical_columns:
        df[f'{col}_add'] = df[col] + 10 

    for col in numerical_columns:
        df[f'{col}_sub'] = df[col] - 10

    for col in numerical_columns:
        df[f'{col}_mul'] = df[col] * 2

    for col in numerical_columns:
        df[f'{col}_div'] = df[col] / 2

    summary_report = {}
    for col in numerical_columns:
        summary_report[col] = {
            'sum': df[col].sum(),
            'mean': df[col].mean(),
            'min': df[col].min(),
            'max': df[col].max(),
            'std': df[col].std()
        }

    summary_df = pd.DataFrame(summary_report).transpose()

    output_file_path = './files/petavue_structured_data_processed.xlsx'
    with pd.ExcelWriter(output_file_path) as writer:
        df.to_excel(writer, sheet_name='Processed Data', index=False)
        summary_df.to_excel(writer, sheet_name='Summary Report')

    print(f"Processed data and summary report saved to {output_file_path}")

def prompt_processing(prompt):
    file_path = './files/petavue_structured_data.xlsx'
    df = pd.read_excel(file_path)
    data = df.head(10)

    code = f'''
    def Solution(file: str) -> str:
        # Write your code here
    '''

    role_prompt = f"you need to write python code: {code} to return the result based upon the command by user for the data stored in xlsx file. The data in file {file_path} is: {data.to_dict(orient='records')}."

    response = openAI_API_Prompt(prompt=prompt, role_prompt=role_prompt ,gpt_model="gpt-4")

    try:
        code_string = response.split('```')[1]

        code_string = code_string.lstrip('python').strip()

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
        result = generated_function(file_path)
        return result
    except Exception as e:
        print(f"Error in generated code: {e}")
        return f"Error: {e}"
