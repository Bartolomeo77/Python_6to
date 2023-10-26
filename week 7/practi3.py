from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
from googlesearch import search  # Importa la biblioteca para buscar en Google.
from duckduckgo_search import DDGS  # Importa la biblioteca para buscar en DuckDuckGo.

# Función para obtener texto desde una URL
def obtener_texto_desde_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text()
    return texto

# Función para obtener URLs relevantes basadas en una consulta
def obtener_urls_relevantes_google(consulta, num_resultados):
    urls = list(search(consulta, num_results=num_resultados))  # Obtener resultados de Google.
    return urls

# Función para obtener URLs relevantes de DuckDuckGo
def obtener_urls_relevantes_ddg(consulta, num_resultados):
    with DDGS() as ddgs:
        # safesearch='off' ==  filtro de búsqueda segura
        # contenido para adultos, lenguaje fuerte o material que podría considerarse inapropiado
        urls = [r['href'] for r in ddgs.text(consulta, safesearch='off', max_results=num_resultados)]
    return urls

# Ejemplo de consulta

consulta = input("Ingresa tu consulta: ")
num_resultados = 2

# Obtener URLs relevantes de Google
urls_relevantes_google = obtener_urls_relevantes_google(consulta, num_resultados)

# Obtener URLs relevantes de DuckDuckGo
urls_relevantes_ddg = obtener_urls_relevantes_ddg(consulta, num_resultados)

# Combinar las URLs relevantes de Google y DuckDuckGo
urls_relevantes = urls_relevantes_google + urls_relevantes_ddg

# Imprimir las URLs relevantes
# 10 de Google y 11 de DuckDuckGo
for i, url in enumerate(urls_relevantes, start=1):
    print(f"{i}. {url}")

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

# Crear una lista de tuplas que contienen la URL y la similitud
urls_similitudes = [(url, similitud) for url, similitud in zip(urls_relevantes, similitudes[0])]

# Ordenar la lista de tuplas por similitud en orden descendente
urls_similitudes = sorted(urls_similitudes, key=lambda x: x[1], reverse=True)

# Mostrar las URLs y similitudes
for i, (url, similitud) in enumerate(urls_similitudes, start=1):
    print(f"Página {i} - URL: {url}")
    print(f"Similitud con la consulta: {similitud:.2f}\n")

pagina_relevante = similitudes.argmax()

# Imprimir la página web más relevante
print("Página web más relevante:", urls_relevantes[pagina_relevante])
print(f"Similitud con la consulta: {urls_similitudes[0][1]:.2f}")



# docker build -t practi3-image .
# docker run practi3-image