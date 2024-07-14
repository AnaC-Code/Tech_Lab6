import pandas as pd

try:
    df = pd.read_csv("Data/Sales.csv", encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv("Data/Sales.csv", encoding='ISO-8859-1')

#df = pd.read_csv("Data/superstore_final_dataset.csv")

# Calculate the number of unique elements per column
unique_counts = df.nunique()

num_records = df.shape[0]
print("Number_of_records ", num_records)
print(unique_counts)
nan_counts = df.isna().sum()
print(f'The number of NaN values in each column is:\n{nan_counts}')
column_dtypes = df.dtypes
print(f'The data types of each column are:\n{column_dtypes}')

last_df = df.drop(columns=["Row_ID","Order_ID","Customer_Name","Country"])
#print(last_df)

last_df.dropna(inplace=True)

last_df.reset_index(drop=True,inplace=True)

last_df['Order_Date'] = pd.to_datetime(last_df['Order_Date'], dayfirst=True)
last_df['Ship_Date'] = pd.to_datetime(last_df['Ship_Date'], dayfirst=True)

print(last_df)

last_df.to_csv("Clea_Data.csv",index=False)


column_dtypes = last_df.dtypes
print(f'The data types of each column are:\n{column_dtypes}')

#Row_ID           deleted
#Order_ID         deleted
#Order_Date       date
#Ship_Date        date
#Ship_Mode        categorical
#Customer_ID      categorical
#Customer_Name    deleted
#Segment          categorical
#Country          deleted
#City             categorical
#State            categorical
#Postal_Code      categorical
#Region           categorical
#Product_ID       categorical
#Category         categorical
#Sub_Category     categorical
#Sales            float64

#Records : 11 records will be deleted because it contains Nan values

