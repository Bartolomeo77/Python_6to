import numpy as np


arr2 = np.array(['banana', 'cherry', 'apple'])
print(arr2)
arr2[0] = "platano"
print(arr2)
print(np.sort(arr2))



arra5 = np.array(['Texto 1', 'Texto 2', 'Texto 3', 'Texto 4', 'Texto 5', 'Texto 6'])
nuevos_indices = [1,2,3,4,5,6]
array_and_indices = np.column_stack((nuevos_indices, arra5))

for row in array_and_indices:
    print(f'Índice: {row[0]}, Valor: {row[1]}')




arr = np.random.randint(0, 100, 10)
print(arr)
print(arr[:5])
print(arr[5:])
print(arr[:2])
print(arr[2:])
print(np.sort(arr))







arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr3[0:2, 2])



arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])



