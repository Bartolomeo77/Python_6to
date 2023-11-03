import numpy as np  

# Definir dos puntos en 2 dimensiones (x, y)
pointA = (1, 1)
pointB = (3, 3)

# Calcular la distancia euclidiana entre los dos puntos
dist = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2  # Calcular la suma de las diferencias al cuadrado
euclidean_dist = np.sqrt(dist)  # Calcular la raíz cuadrada de la suma


def manhattan_distance(point1, point2):
    # point1 y point2 son tuplas que representan los puntos en formato (x, y)
    x1, y1 = point1
    x2, y2 = point2
    # Calcular la distancia de Manhattan
    distance = abs(x1 - x2) + abs(y1 - y2)
    
    return distance
distance = manhattan_distance(pointA, pointB)

print(f"La distancia de euclidiana {euclidean_dist}")
print(f"La distancia de Manhattan {distance}")
