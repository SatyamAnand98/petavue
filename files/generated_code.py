import pandas as pd

def Solution(file: str) -> str:
    # Load data
    data = pd.read_excel(file)
    
    # Calculate new salaries
    data.loc[data['Department'] == 'IT', 'Salary'] = data.loc[data['Department'] == 'IT', 'Salary'] + 100
    
    # Save modified data to new file
    new_file = './files/modified_structured_data.xlsx'
    data.to_excel(new_file, index=False)
    
    return new_file