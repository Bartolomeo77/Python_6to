import numpy as np
import pandas as pd

print("Empleando series")

arr2 = np.array(['banana', 'cherry', 'apple'])
arr2[0] = "platano"

print(" 2 ")

arra5 = np.array(['Texto 1', 'Texto 2', 'Texto 3'])
nuevos_indices = [1,2,3]
array_and_indices = np.column_stack((nuevos_indices, arra5))

for row in array_and_indices:
    print(f'Índice: {row[0]}, Valor: {row[1]}')


print(" 3 ")

arr = np.random.randint(0, 100, 10)
print(arr)
print(arr[:5])
print(arr[5:])
print(arr[:2])
print(arr[2:])
print(np.sort(arr))

print("Empleando DataFrame1")

arreglo = {
    'Texto': ['Texto 1', 'Texto 2', 'Texto 3', 'Texto 4', 'Texto 5', 'Texto 6'],
    'Valor': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(arreglo)
print(df)


df = df[['Valor', 'Texto']]


print(df)

print("Leer archivos Ventas.csv")

Pyventas = pd.read_csv("Ventas.csv", sep=";")

print(Pyventas)

print("Empleando DataFrame 2")
OneArreglo = {
    'Texto1': ['Texto 1', 'Texto 2', 'Texto 3', 'Texto 4', 'Texto 5', 'Texto 6'],
    'Valor1': [10, 20, 30, 40, 50, 60]
}

df1 = pd.DataFrame(OneArreglo)

TwoArreglo = {
    'Texto2': ['Texto A', 'Texto B', 'Texto C', 'Texto D', 'Texto E', 'Texto F'],
    'Valor2': [70, 80, 90, 100, 110, 120]
}

df2 = pd.DataFrame(TwoArreglo)

df_final = pd.concat([df1, df2], axis=1)

print(df_final)

print("Empleando DataFrame 3")

# Leer el archivo CSV


Pyventas = pd.read_csv("Ventas.csv", sep=";")

ventas_primer_trimestre = Pyventas["Monto"]
print("Ventas del primer trimestre:")
print(ventas_primer_trimestre)

# b. Imprima el número de registros y el número de campos


num_registros, num_campos = Pyventas.shape
print(f"Número de registros: {num_registros}")
print(f"Número de campos: {num_campos}")

# c. Genere un arreglo numérico con las ventas del primer trimestre del año y realice cálculos estadísticos

ventas_numericas = Pyventas["Monto"]

media = ventas_numericas.mean()
print(f"Media de ventas: {media}")

correlacion = ventas_numericas.corr(ventas_numericas)
print(f"Correlación de ventas: {correlacion}")

valor_minimo = ventas_numericas.min()
print(f"Valor más bajo de ventas: {valor_minimo}")

valor_maximo = ventas_numericas.max()
print(f"Valor más alto de ventas: {valor_maximo}")

mediana = ventas_numericas.median()
print(f"Mediana de ventas: {mediana}")

desviacion_estandar = ventas_numericas.std()
print(f"Desviación estándar de ventas: {desviacion_estandar}")

print("Primera columna del dataset:")
print(Pyventas.iloc[:, 0])

print("Dos primeras columnas del dataset:")
print(Pyventas.iloc[:, :2])

print("Primera fila y última columna:")
print(Pyventas.iloc[0, -1])

print("Valores de la primera fila:")
print(Pyventas.iloc[0, :].values)











print("Leer archivos Ventas2.csv")

PyVentas02 = pd.read_excel("Ventas02.xlsx", header=None, skiprows=1)

print(PyVentas02)
