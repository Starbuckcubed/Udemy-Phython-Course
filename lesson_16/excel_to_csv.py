import pandas as pd

def convert_excel_to_csv(excel_file):
    df = pd.read_excel(excel_file)
    csv_data = df.to_csv(index=False)
    return csv_data
