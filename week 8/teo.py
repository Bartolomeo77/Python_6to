import numpy as np  

# Definir dos puntos en 2 dimensiones (x, y)
p1 = (1, 1)
p2 = (2, 2)

# Calcular la distancia euclidiana entre los dos puntos
dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2  # Calcular la suma de las diferencias al cuadrado
euclidean_dist = np.sqrt(dist)  # Calcular la raíz cuadrada de la suma
print(euclidean_dist)  # Imprimir la distancia euclidiana










# Definir dos puntos en 3 dimensiones (x, y, z)
p1 = (1, 1, 1)
p2 = (2, 2, 2)

# Calcular la distancia euclidiana entre los dos puntos en 3 dimensiones
dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2  # Calcular la suma de las diferencias al cuadrado
euclidean_dist = np.sqrt(dist)  # Calcular la raíz cuadrada de la suma
print(euclidean_dist)  # Imprimir la distancia euclidiana

# Definir dos puntos en 4 dimensiones (x, y, z, w)
p1 = (1, 1, 1, 1)
p2 = (2, 2, 2, 2)

dist = 0  # Inicializar la variable "distancia" en cero

# Calcular la distancia euclidiana entre los dos puntos en 4 dimensiones usando un bucle "for"
for i in range(len(p1)):
  dist = dist + (p1[i] - p2[i])**2  # Acumular la suma de las diferencias al cuadrado

euclidean_dist = np.sqrt(dist)  # Calcular la raíz cuadrada de la suma
print(euclidean_dist)  # Imprimir la distancia euclidiana

# Definir una función para calcular la distancia euclidiana entre dos puntos en cualquier número de dimensiones
def get_euclidean_distance(p1, p2):
  dist = 0  # Inicializar la variable "distancia" en cero

  # Calcular la distancia euclidiana usando un bucle "for"
  for i in range(len(p1)):
    dist = dist + (p1[i] - p2[i])**2  # Acumular la suma de las diferencias al cuadrado

  euclidean_dist = np.sqrt(dist)  # Calcular la raíz cuadrada de la suma
  print(euclidean_dist)  # Imprimir la distancia euclidiana

# Llamar a la función con dos puntos en 3 dimensiones
get_euclidean_distance((1, 1, 1), (2, 2, 2))



# Definir una función para calcular la distancia de Manhattan entre dos puntos en cualquier número de dimensiones
def get_manhattan_distance(p1, p2):
  dist = 0  # Inicializar la variable "distancia" en cero

  # Calcular la distancia de Manhattan usando un bucle "for"
  for i in range(len(p1)):
    dist = dist + abs(p1[i] - p2[i])  # Acumular la suma de las diferencias absolutas

  manhattan_dist = dist  # Asignar la distancia de Manhattan
  print(manhattan_dist)  # Imprimir la distancia de Manhattan

# Llamar a la función con dos puntos en 4 dimensiones
get_manhattan_distance((1, 1, 1, 1), (2, 2, 2, 2))

# Imprimir el valor absoluto de la resta de dos números
print(abs(1 - 2))  # Imprimir el valor absoluto de la resta

# Calcular y mostrar la distancia euclidiana y de Manhattan entre dos conjuntos de datos específicos
print(get_euclidean_distance((63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1), (37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2)))
print(get_manhattan_distance((63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1), (37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2)))
