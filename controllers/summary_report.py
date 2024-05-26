import pandas as pd

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
