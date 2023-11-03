import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:123456789@localhost/sakila')

def cargar_tabla(tabla):
    query = f"SELECT * FROM {tabla}"
    # Utiliza pd.read_sql para ejecutar la consulta y cargar los resultados en un DataFrame de Pandas.
    df = pd.read_sql(query, engine)
    return df


TablCustomer = cargar_tabla('customer') 

#.head() para mostrar las primeras filas del DataFrame
print(TablCustomer.head()) 



def estadisticas_cliente(df):
    cliente_df = cargar_tabla(df) 
    print("Estadísticas de la tabla {df} :")
    # .describe() generar un resumen estadístico de un DataFrame 
    print(cliente_df.describe())

estadisticas_cliente("customer")

def tendencia_central_pagos_payment():
    pago_df = cargar_tabla("payment") 
    print("Tendencia central de la tabla Payment - Cantidad (amount):")
    #pago_df['amount'].mean() la media aritmética de los valores en la columna 'amount'
    print("Media:", pago_df['amount'].mean())
    #pago_df['amount'].median() la Mediana aritmética de los valores en la columna 'amount'
    print("Mediana:", pago_df['amount'].median())
    #pago_df['amount'].mode() la moda de los  !valores¡ en la columna 'amount',se toma el primer valor de la serie de moda, que se obtiene con [0].
    print("Moda:", pago_df['amount'].mode()[0])

tendencia_central_pagos_payment()

def tendencia_central_pelicula():
    pelicula_df = cargar_tabla("film") 
    print("Tendencia central de la tabla Film - Costo de reemplazo (Replacement_cost):")
    print("Media:", pelicula_df['replacement_cost'].mean())
    print("Mediana:", pelicula_df['replacement_cost'].median())
    print("Moda:", pelicula_df['replacement_cost'].mode()[0])

tendencia_central_pelicula()

def tendencia_central_pagos_peru():

    query = """
    SELECT p.amount
    FROM payment AS p
    JOIN customer AS c ON p.customer_id = c.customer_id
    JOIN address AS a ON c.address_id = a.address_id
    JOIN city AS ct ON a.city_id = ct.city_id
    JOIN country AS co ON ct.country_id = co.country_id
    WHERE co.country = 'Peru'
    """
    peru_df = pd.read_sql(query, engine)
    
    print("Tendencia central de la tabla Payment - Cantidad (amount) de los clientes de Perú:")
    print("Media:", peru_df['amount'].mean())
    print("Mediana:", peru_df['amount'].median())
    print("Moda:", peru_df['amount'].mode()[0])

tendencia_central_pagos_peru()