import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Cargar el archivo CSV
clientes = pd.read_csv("Movie_Ratings.csv")

# Seleccionar las columnas de calificaciones como características (X) y la película a predecir como objetivo (y)
X = clientes.iloc[:, 1:]  # Excluye la columna "peliculas"
y = clientes["peliculas"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un imputador para llenar los valores faltantes con la media
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Escalar las características para normalizarlas
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear un clasificador KNN
knn = KNeighborsClassifier(n_neighbors=1)  # Puedes ajustar el número de vecinos

# Entrenar el modelo
knn.fit(X_train, y_train)

# Predecir las películas en el conjunto de prueba
y_pred = knn.predict(X_test)

# Evaluar el rendimiento del modelo
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo KNN:", accuracy)
