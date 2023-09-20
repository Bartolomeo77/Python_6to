import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('Panamericanos_Lima.csv')

# a. Sumatoria de los valores de una columna (por ejemplo, la columna 'Oro')
suma_de_oro = df['Oro'].sum()
print("Sumatoria de Oro:", suma_de_oro)

# b. Número de elementos (filas)
num_elementos = len(df)
print("Número de elementos:", num_elementos)

# c. Media
media = df['Oro'].mean()
print("Media:", media)

# d. Media redondeada a 2 decimales
media_redondeada = round(media, 2)
print("Media redondeada:", media_redondeada)

# e. Mediana
mediana = df['Oro'].median()
print("Mediana:", mediana)

# f. Moda
moda = df['Oro'].mode()
print("Moda:", moda)

# g. Percentiles (por ejemplo, el percentil 25%)
percentil_25 = df['Oro'].quantile(0.25)
print("Percentil 25:", percentil_25)

# h. Varianza
varianza = df['Oro'].var()
print("Varianza:", varianza)
