import pandas as pd

# Load the data
file_path = '17072024_sales_data/Clean_Data.csv'
data = pd.read_csv(file_path)

# Display basic information about the dataset
data_info = data.info()
data_head = data.head()
data_description = data.describe(include='all')

print(data_info)
print(data_head) 
print(data_description)

import matplotlib.pyplot as plt
import seaborn as sns

# Convert Order_Date and Ship_Date to datetime format
data['Order_Date'] = pd.to_datetime(data['Order_Date'])
data['Ship_Date'] = pd.to_datetime(data['Ship_Date'])

# Check for missing values
missing_values = data.isnull().sum()

# Sales distribution by Category
sales_by_category = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# Sales distribution by Sub_Category
sales_by_sub_category = data.groupby('Sub_Category')['Sales'].sum().sort_values(ascending=False)

# Sales distribution by Region
sales_by_region = data.groupby('Region')['Sales'].sum().sort_values(ascending=False)

# Sales distribution by Segment
sales_by_segment = data.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

# Shipping mode analysis
ship_mode_analysis = data['Ship_Mode'].value_counts()

# Plotting Sales distribution by Category
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values, palette='viridis')
plt.title('Sales Distribution by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.show()

# Plotting Sales distribution by Sub_Category
plt.figure(figsize=(12, 8))
sns.barplot(x=sales_by_sub_category.index, y=sales_by_sub_category.values, palette='viridis')
plt.title('Sales Distribution by Sub-Category')
plt.ylabel('Sales')
plt.xlabel('Sub-Category')
plt.xticks(rotation=90)
plt.show()

# Plotting Sales distribution by Region
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_region.index, y=sales_by_region.values, palette='viridis')
plt.title('Sales Distribution by Region')
plt.ylabel('Sales')
plt.xlabel('Region')
plt.show()

# Plotting Sales distribution by Segment
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_segment.index, y=sales_by_segment.values, palette='viridis')
plt.title('Sales Distribution by Segment')
plt.ylabel('Sales')
plt.xlabel('Segment')
plt.show()

# Plotting Ship Mode Analysis
plt.figure(figsize=(10, 6))
sns.countplot(x=data['Ship_Mode'], palette='viridis')
plt.title('Shipping Mode Distribution')
plt.ylabel('Count')
plt.xlabel('Ship Mode')
plt.show()

# Summary of findings
missing_values, sales_by_category, sales_by_sub_category, sales_by_region, sales_by_segment, ship_mode_analysis

# Time-Series Analysis: Monthly and Yearly Sales Trends
data['Order_Month'] = data['Order_Date'].dt.to_period('M')
data['Order_Year'] = data['Order_Date'].dt.year

# Monthly Sales Trend
monthly_sales = data.groupby('Order_Month')['Sales'].sum()

# Yearly Sales Trend
yearly_sales = data.groupby('Order_Year')['Sales'].sum()

# Plotting Monthly Sales Trend
plt.figure(figsize=(14, 7))
monthly_sales.plot()
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plotting Yearly Sales Trend
plt.figure(figsize=(10, 6))
yearly_sales.plot(kind='bar')
plt.title('Yearly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Year')
plt.grid(True)
plt.show()


# Correlation Analysis: Focusing on Sales and Ship_Mode
# Creating a correlation matrix
correlation_matrix = data.corr()


# Customer Analysis: Sales by State and City
sales_by_state = data.groupby('State')['Sales'].sum().sort_values(ascending=False)
sales_by_city = data.groupby('City')['Sales'].sum().sort_values(ascending=False)

# Plotting Sales by State
plt.figure(figsize=(14, 7))
sales_by_state.head(20).plot(kind='bar')
plt.title('Top 20 States by Sales')
plt.ylabel('Sales')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.show()

# Plotting Sales by City
plt.figure(figsize=(14, 7))
sales_by_city.head(20).plot(kind='bar')
plt.title('Top 20 Cities by Sales')
plt.ylabel('Sales')
plt.xlabel('City')
plt.xticks(rotation=45)
plt.show()

# Shipping and Delivery: Calculating Delivery Time
data['Delivery_Time'] = (data['Ship_Date'] - data['Order_Date']).dt.days

# Delivery Time Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Delivery_Time'], bins=20, kde=True)
plt.title('Delivery Time Distribution')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Impact of Ship Mode on Delivery Time
plt.figure(figsize=(10, 6))
sns.boxplot(x='Ship_Mode', y='Delivery_Time', data=data, palette='viridis')
plt.title('Impact of Ship Mode on Delivery Time')
plt.xlabel('Ship Mode')
plt.ylabel('Delivery Time (Days)')
plt.grid(True)
plt.show()

# Summary of analyses
monthly_sales_summary = monthly_sales.describe()
yearly_sales_summary = yearly_sales.describe()
delivery_time_summary = data['Delivery_Time'].describe()

#correlation_matrix,
sales_by_state.head(10), sales_by_city.head(10), monthly_sales_summary, yearly_sales_summary, delivery_time_summary

# Deep Dive into High Sales States and Cities

# Top 10 customers by sales
top_customers = data.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(10)

# Plotting Top 10 Customers by Sales
plt.figure(figsize=(12, 6))
sns.barplot(x=top_customers.index, y=top_customers.values, palette='viridis')
plt.title('Top 10 Customers by Sales')
plt.ylabel('Sales')
plt.xlabel('Customer ID')
plt.xticks(rotation=45)
plt.show()

# Analyzing purchasing behavior of top customers
top_customers_data = data[data['Customer_ID'].isin(top_customers.index)]

# Sales by top customers over time
top_customers_monthly_sales = top_customers_data.groupby(['Customer_ID', 'Order_Month'])['Sales'].sum().unstack('Customer_ID')

# Plotting Sales by Top Customers Over Time
plt.figure(figsize=(14, 7))
top_customers_monthly_sales.plot()
plt.title('Monthly Sales Trend for Top 10 Customers')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.legend(title='Customer ID')
plt.grid(True)
plt.show()

# Further Shipping Analysis: Cost-effectiveness of different shipping modes
# Assuming we have a shipping cost data (mock data for the sake of analysis)
# Example cost data: {'Standard Class': 5, 'Second Class': 10, 'First Class': 20, 'Same Day': 50}
shipping_costs = {'Standard Class': 5, 'Second Class': 10, 'First Class': 20, 'Same Day': 50}
data['Shipping_Cost'] = data['Ship_Mode'].map(shipping_costs)

# Calculate total shipping cost for each mode
total_shipping_cost = data.groupby('Ship_Mode')['Shipping_Cost'].sum()

# Calculate total sales for each shipping mode
total_sales_by_ship_mode = data.groupby('Ship_Mode')['Sales'].sum()

# Cost-effectiveness ratio: Sales per unit shipping cost
cost_effectiveness = total_sales_by_ship_mode / total_shipping_cost

# Plotting Cost-effectiveness of Different Shipping Modes
plt.figure(figsize=(12, 6))
sns.barplot(x=cost_effectiveness.index, y=cost_effectiveness.values, palette='viridis')
plt.title('Cost-effectiveness of Different Shipping Modes')
plt.ylabel('Sales per Unit Shipping Cost')
plt.xlabel('Shipping Mode')
plt.xticks(rotation=45)
plt.show()

# Customer satisfaction analysis based on delivery times and shipping modes
# Assuming customer satisfaction score is inversely proportional to delivery time
data['Satisfaction_Score'] = 10 - data['Delivery_Time']

# Average satisfaction score by shipping mode
avg_satisfaction_by_ship_mode = data.groupby('Ship_Mode')['Satisfaction_Score'].mean()

# Plotting Average Satisfaction Score by Shipping Mode
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_satisfaction_by_ship_mode.index, y=avg_satisfaction_by_ship_mode.values, palette='viridis')
plt.title('Average Satisfaction Score by Shipping Mode')
plt.ylabel('Satisfaction Score')
plt.xlabel('Shipping Mode')
plt.xticks(rotation=45)
plt.show()

# Summary of analyses
top_customers, total_shipping_cost, total_sales_by_ship_mode, cost_effectiveness, avg_satisfaction_by_ship_mode
