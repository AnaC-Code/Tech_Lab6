# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset
df = pd.read_csv('C:\\Users\\Ricardo.Jordan\\Github\\Tech_Lab6\\Data\\superstore_final_dataset.csv', encoding='latin1')


# 3. Understand Structure
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df.head())
#print(df.describe())
#print(df.info())

#Data Cleaning
#Convert fields into the correct data types
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d/%m/%Y', errors='coerce')
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], format='%d/%m/%Y', errors='coerce')

categorical_columns = ['Ship_Mode', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'Sub_Category', 'Product_ID' ]
for col in categorical_columns:
    df[col] = df[col].astype('category')

numerical_columns = ['Postal_Code', 'Sales']
for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')



# Check for missing values
missing_values = df.isnull().sum()

# 3. Data Consistency
# Check for duplicates
df.drop_duplicates(inplace=True)

print(df.info())
"""
#Exploratory Data Analysis (EDA)
# Sales by Category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

#Sales by Region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()
"""
# Time series analysis of Sales
df.set_index('Order_Date', inplace=True)
sales_over_time = df['Sales'].resample('M').sum()
plt.figure(figsize=(14, 7))
sales_over_time.plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()


"""
# Correlation analysis
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

"""