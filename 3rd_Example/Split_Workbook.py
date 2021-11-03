import pandas as pd #pip install pandas
import os

df = pd.read_excel('Financial_Sample.xlsx')
column_name = 'Country'
replace_symbols = ['>', '<', ':', '"', '/', '\\\\', '\|', '\?', '\*']
df[column_name] = (
    df[column_name].replace(replace_symbols, '', regex=True).str.strip().str.title()
)
unique_values = df[column_name].unique()

for unique_value in unique_values:
    df_output = df[df[column_name].str.contains(unique_value)]
    output_path = os.path.join('output', str(unique_value) + '.xlsx')
    df_output.to_excel(output_path, sheet_name=unique_value[:31], index=False)
