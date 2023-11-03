from googlesearch import search  # Importa la biblioteca para buscar en Google.


query = "que es seo?"
num_resultss = 5  # Ajusta el número de resultados que deseas.

results = list(search(query, num_results=num_resultss))

for result in results:
    print(result)


def obtener_urls_relevantes(consulta, num_resultados):
    urls = list(search(consul, num_results=num_resultados))  # Obtener más resultados.
    return urls

# Ejemplo de consulta
consulta = "que dia es hoy?"
urls_relevantes = obtener_urls_relevantes(consulta, 5)  # Ajusta el número de resultados deseado.

