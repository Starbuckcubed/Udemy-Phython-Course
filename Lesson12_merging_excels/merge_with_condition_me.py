import pandas as pd
import os

directory = 'excel_years'

filenames = os.listdir(directory)

filepaths = [os.path.join(directory, f) for f in os.listdir(directory)]
#goes to each of the file names for each of them we generate a list of paths
#construct a list of all of the strings
# Generate filepaths for files which include '2024' and '2025' in their names
filepaths_2024 = [fp for fp in filepaths if '2024' in os.path.basename(fp)]
filepaths_2025 = [fp for fp in filepaths if '2025' in os.path.basename(fp)]

dataframes_2024 = [pd.read_excel(filepath) for filepath in filepaths_2024]
dataframes_2025 = [pd.read_excel(filepath) for filepath in filepaths_2025]

merged_df_2024 = pd.concat(dataframes_2024, ignore_index=True)
merged_df_2025 = pd.concat(dataframes_2025, ignore_index=True)

#export the merged data frames into a new excel file
merged_df_2024.to_excel('excel_years/merged_excel_2024.xlsx', index=False)
merged_df_2025.to_excel('excel_years/merged_excel_2025.xlsx', index=False)