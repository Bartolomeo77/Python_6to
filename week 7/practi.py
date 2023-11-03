# 1. Importar las bibliotecas necesarias
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup


# 2. Rastrear y recopilar documentos de las páginas web

def obtener_texto_desde_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text()
    return texto



# Ejemplo de recopilación de texto desde una página web
url1 = "https://rockcontent.com/es/blog/que-es-seo/"
url2 = "https://www.40defiebre.com/guia-seo/que-es-seo-por-que-necesito"
url3 = "https://es.semrush.com/blog/que-es-seo/"
documento_web1 = obtener_texto_desde_url(url1)
documento_web2 = obtener_texto_desde_url(url2)
documento_web3 = obtener_texto_desde_url(url3)

# 3. Limpiar y preprocesar el texto de las páginas
documentos = [documento_web1, documento_web2,documento_web3]

# 4. Calcular TF-IDF para los términos de las páginas web

vectorizador = TfidfVectorizer()
tfidf_matrix = vectorizador.fit_transform(documentos)




# 5. Realizar una consulta y encontrar las páginas web relevantes
consulta = "que es seo ?"

consulta_tfidf = vectorizador.transform([consulta])

similitudes = cosine_similarity(consulta_tfidf, tfidf_matrix)

# Obtener el índice de la página web más relevante
# Argmax() es una libreria de numpy
# similitudes.argmax() encuentra el índice del valor máximo en la matriz similitudes, que corresponde a la página web más relevante en función de la consulta.
pagina_relevante = similitudes.argmax()

# Imprimir la página web más relevante
print("Página web más relevante:", f"URL: {pagina_relevante}")
