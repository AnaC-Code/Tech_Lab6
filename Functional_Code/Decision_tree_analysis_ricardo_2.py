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

#Data Cleaning
#Convert fields into the correct data types
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d/%m/%Y', errors='coerce')
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], format='%d/%m/%Y', errors='coerce')

categorical_columns = ['Ship_Mode', 'Segment', 'City', 'State', 'Region', 'Category', 'Sub_Category', 'Product_ID' ]
for col in categorical_columns:
    df[col] = df[col].astype('category')




numerical_columns = ['Postal_Code', 'Sales']
for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


# Preprocesamiento para datos categóricos (one-hot encoding)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical_columns),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
    ])


#Separar las características (features) de la variable objetivo (target)
# Usar una lista de columnas a eliminar y especificar axis=1 para eliminar columnas
columns_to_drop = [ 'State', 'Postal_Code', 'Region', 'Product_ID', 'Order_Date', 'Ship_Date']
X = df.drop(columns=columns_to_drop, axis=1)
y = df['Sales']  # Variable objetivo

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline con preprocesamiento y modelo
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', DecisionTreeRegressor(random_state=42))
])

# Dividir los datos en conjunto de entrenamiento y prueba
X = df.drop(columns=['Sales'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred = pipeline.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Error Cuadrático Medio (MSE): {mse}')
print(f'Coeficiente de Determinación (R^2): {r2}')

# Obtener la importancia de las características
model = pipeline.named_steps['model']
importances = model.feature_importances_

# Obtener los nombres de las características transformadas
encoded_features = pipeline.named_steps['preprocessor'].transformers_[1][1].get_feature_names_out(categorical_columns)
all_features = numerical_columns + encoded_features.tolist()

# Crear un DataFrame con las importancias de las características
feature_importances = pd.DataFrame({'Feature': all_features, 'Importance': importances})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

print("Importancia de las características:")
print(feature_importances.head(10))




#Inicializar el modelo 

# model = DecisionTreeRegressor (random_state=42)
# model.fit(X_train, y_train)

# # Hacer predicciones sobre el conjunto de prueba
# y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f'Error Cuadrático Medio (MSE): {mse}')
# print(f'Coeficiente de Determinación (R^2): {r2}')

# Visualizar resultados
# plt.figure(figsize=(10, 6))
# plt.scatter(y_test, y_pred, alpha=0.5)
# plt.xlabel('Ventas Reales')
# plt.ylabel('Ventas Predichas')
# plt.title('Ventas Reales vs Ventas Predichas')
# plt.show()

# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, y)
# tree.plot_tree(clf)

