from googlesearch import search  # Importa la biblioteca para buscar en Google.


query = "que es seo?"
num_resultss = 5  # Ajusta el número de resultados que deseas.

results = list(search(query, num_results=num_resultss))

for result in results:
    print(result)
