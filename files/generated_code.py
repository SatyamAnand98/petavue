import pandas as pd
from typing import List

def Solution(file: str) -> List[str]:
    df = pd.read_excel(file)
    
    highest_earning_people = df.loc[df.groupby("Department")["Salary"].idxmax()][['Name', 'Department']].values.tolist()  
    return highest_earning_people