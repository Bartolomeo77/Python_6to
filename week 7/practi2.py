from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
from googlesearch import search  # Importa la biblioteca para buscar en Google.


# Función para obtener texto desde una URL
def obtener_texto_desde_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text()
    return texto

# Función para obtener URLs relevantes basadas en una consulta
def obtener_urls_relevantes(consulta, num_resultados):
    urls = list(search(consulta, num_results=num_resultados))  # Obtener más resultados.
    return urls

# Ejemplo de consulta
consulta = "que es seo?"
urls_relevantes = obtener_urls_relevantes(consulta,5)  # Ajusta el número de resultados deseado.


# Lista para almacenar documentos web
documentos = []

# Recopila el contenido de las URLs relevantes
for url in urls_relevantes:
    documento_web = obtener_texto_desde_url(url)
    documentos.append(documento_web)

# Preprocesamiento del texto, cálculo de TF-IDF y búsqueda de la página más relevante

vectorizador = TfidfVectorizer()
tfidf_matrix = vectorizador.fit_transform(documentos)

consulta_tfidf = vectorizador.transform([consulta])
similitudes = cosine_similarity(consulta_tfidf, tfidf_matrix)


# ------------ 

urls_similitudes = [(url, similitud) for url, similitud in zip(urls_relevantes, similitudes[0])]



urls_similitudes = sorted(urls_similitudes, key=lambda x: x[1], reverse=True)


# Mostrar las URLs y similitudes
for i, (url, similitud) in enumerate(urls_similitudes, start=1):
    print(f"Página {i} - URL: {url}")
    print(f"Similitud con la consulta: {similitud:.2f}\n")


pagina_relevante = similitudes.argmax()

# Imprimir la página web más relevante
print("Página web más relevante:", urls_relevantes[pagina_relevante])
print(f"Similitud con la consulta: {urls_similitudes[0][1]:.2f}")
