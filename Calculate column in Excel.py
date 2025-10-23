import pandas as pd

output_total = pd.read_excel('input.xlsx')



print(output_total.head())
print(output_total.info())
print(output_total.describe())

output_total['total'] = output_total['Price'] * output_total ['Quantity']

print(output_total)

output_total.to_csv('output.csv', index=False)