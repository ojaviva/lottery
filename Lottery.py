import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.multioutput import MultiOutputRegressor

# Paso 1: Cargar los datos desde el archivo Excel
df = pd.read_excel('num.xlsx')

# Paso 2: Preprocesar los datos
X = df.loc[:, ['sum_num', 'promedio', 'minimo', 'maximo', 'rango', 'desviacion_estandar', 'mediana',  'mes_sorteo', 'año_sorteo']]
y = df.loc[:, ['num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6']]

# Paso 3: Dividir los datos en conjuntos de entrenamiento, validación y prueba
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Paso 4: Entrenar un modelo de árbol de decisión ajustando sus hiperparámetros
tree_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
multi_target_tree = MultiOutputRegressor(tree_reg)
multi_target_tree.fit(X_train, y_train)

# Paso 5: Realizar predicciones en el conjunto de prueba
test_predictions = multi_target_tree.predict(X_test)

# Paso 6: Redondear las predicciones a números enteros
test_predictions_discretos = test_predictions.round().astype(int)

# Mostrar las predicciones discretas
print("Predicciones discretas en conjunto de prueba:")
print(test_predictions_discretos)

# Preparar los datos para la predicción del sorteo número 2334
ultimo_sorteo = df.iloc[-1][['sum_num', 'promedio', 'minimo', 'maximo', 'rango', 'desviacion_estandar', 'mediana', 'mes_sorteo', 'año_sorteo']].values.reshape(1, -1)

# Realizar la predicción para el sorteo número 2334
prediccion_2334 = multi_target_tree.predict(ultimo_sorteo)

# Redondear la predicción a números enteros
prediccion_2334_discreta = prediccion_2334.round().astype(int)

# Mostrar la predicción discreta
print("Predicción discreta para el sorteo número 2334:")
print(prediccion_2334_discreta)
