import pandas as pd

# .size Devuelve el numero de elementos de la serie

# .index Devuelve una lista con los nombres de las filas de DataFrame
# .dtype Devuelve el tipo de datos de los elementos de la serie


colores = pd.Series(['rojo','azul','amarrillo','verde','morado'])
print(colores)


colores2 = pd.Series({'Matematicas':60,'Fisica':100,'Quimica':78})
print(colores2)

