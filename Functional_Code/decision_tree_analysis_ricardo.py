import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline



df = pd.read_csv ('C:\\Users\\Ricardo.Jordan\\Github\\Tech_Lab6\\17072024_sales_data\Clean_Data.csv', encoding='latin1')

#Datos de ventas
#print(df[:5])

# Verificar valores nulos
#print(df.isnull().sum())

# Eliminar filas con valores nulos (si hay)
#df = df.dropna()

# 1 Data Cleaning
#Convert fields into the correct data types




# Convert the string dates to datetime objects

df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], errors='coerce')

# Extract year, month, and day from Order_Date
df['Order_Year'] = df['Order_Date'].dt.year
df['Order_Month'] = df['Order_Date'].dt.month
df['Order_Day'] = df['Order_Date'].dt.day

# Extract year, month, and day from Ship_Date
df['Ship_Year'] = df['Ship_Date'].dt.year
df['Ship_Month'] = df['Ship_Date'].dt.month
df['Ship_Day'] = df['Ship_Date'].dt.day




#Drop original date columns
date_cols = ['Order_Date', 'Ship_Date']
df = df.drop(columns=date_cols)

categorical_columns = ['Ship_Mode', 'Segment', 'City', 'State', 'Region', 'Category', 'Sub_Category', 'Product_ID' ]
for col in categorical_columns:
    df[col] = df[col].astype('category')


numerical_columns = ['Postal_Code', 'Sales']
for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')





# Asegurarse de que la columna objetivo existe y tiene el nombre correcto
if 'Sales' not in df.columns:
    raise ValueError("La columna 'Sales' no se encuentra en el DataFrame.")


# Preprocesamiento de datos: contar y eliminar filas con valores nulos
# initial_row_count = df.shape[0]
# df = df.dropna()
# final_row_count = df.shape[0]
# rows_dropped = initial_row_count - final_row_count

#print(final_row_count)

# Identify categorical columns
categorical_columns = ['Ship_Mode', 'Segment', 'City', 'State', 'Region', 'Category', 'Sub_Category', 'Product_ID']

# Apply one-hot encoding to categorical columns
df = pd.get_dummies(df, columns=categorical_columns)


#Separar las características (features) de la variable objetivo (target)

# Features = ['Order_Date', 'Ship_Date', 'Ship_Mode', 'Customer_ID', 'Segment', 
#             'City', 'State', 'Postal_Code', 'Region', 'Product_ID', 'Category', 
#             'Sub_Category', 'Product_Name', 'Order_Year', 'Order_Month', 'Order_Day', 
#             'Ship_Year', 'Ship_Month', 'Ship_Day']

columns_to_drop = [ 'Sales','Customer_ID','Product_Name',  'Postal_Code']
X = df.drop(columns=columns_to_drop, axis=1)
y = df['Sales']  # Variable objetivo



# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializar el modelo 

model = DecisionTreeRegressor (random_state=42)
model.fit(X_train, y_train)


# Hacer predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Error Cuadrático Medio (MSE): {mse}')
print(f'Coeficiente de Determinación (R^2): {r2}')

print(df.head)

print(df.dtypes)