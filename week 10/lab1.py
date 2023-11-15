import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Cargar el DataFrame con las calificaciones
clientes = pd.read_csv("Movie_Ratings.csv")

# Seleccionar el vector de "vanessa" y eliminar los valores nulos
vanessa_vector = clientes.loc["vanessa"].dropna().values.reshape(1, -1)

# Calcular la similitud del coseno entre "vanessa" y todos los demás clientes
similarity_matrix = cosine_similarity(clientes.dropna(), vanessa_vector)

# Crear un DataFrame con las similitudes
similarity_df = pd.DataFrame(similarity_matrix, index=clientes.dropna().index, columns=["Similarity"])

# Encontrar los 3 vecinos más cercanos a "vanessa"
nearest_neighbors = similarity_df.nlargest(3, "Similarity")

print(nearest_neighbors)
