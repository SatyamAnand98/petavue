import pandas as pd

def Solution(file: str) -> str:
    df = pd.read_excel(file)
    
    # Update salary of employees in IT department
    mask = df['Department'] == 'IT' 
    df.loc[mask, 'Salary'] = df.loc[mask, 'Salary'] + 100
    
    # Save modified dataset to new file
    df.to_excel("./files/modified_structured_data.xlsx", index=False)
    
    return df.to_dict(orient='records')

print(Solution("./files/structured_data.xlsx"))