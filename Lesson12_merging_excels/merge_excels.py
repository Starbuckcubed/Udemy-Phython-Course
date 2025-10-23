import pandas as pd
import os

directory = 'excel_files'

filenames = os.listdir(directory)
#goes to each of the file names for each of them we generate a list of paths
#construct a list of all of the strings
filepaths = [os.path.join(directory, filename) for filename in filenames]

#now we can iterate over the filepaths, comes from panda, table
# dataframes =[]
# for filepath in filepaths:
#     #open as data frames
#     df = pd.read_excel(filepath)
#     dataframes.append(df)

#list comprehension of the for loop above
#the data frames are now stored in a list
dataframes = [pd.read_excel(filepath) for filepath in filepaths]

#export the data frames to a new file
#when pandas saves the dataframe it adds a column with incremental integers the ignore command ignores that column
merged_df = pd.concat(dataframes, ignore_index=True)
print(merged_df)

#export the merged data frames into a new excel file
merged_df.to_excel('excel_files/merged_excel.xlsx', index=False)