import pandas as pd

# Load the Excel file
df = pd.read_excel('superstore_final_dataset (1).xlsx')

# Display the first few rows
print(df.head())

# Display column names
print(df.columns)

# Display data types
print(df.dtypes)

# Drop columns by name
df = df.drop(columns=['Customer_Name', 'Country'])

# Drop rows with any missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned data
df.to_excel('cleaned_excel_file_20240714.xlsx', index=False)

print("Data cleaning complete and saved to 'cleaned_excel_file_20240714.xlsx'")


