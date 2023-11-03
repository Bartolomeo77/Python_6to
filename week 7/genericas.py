import requests
from bs4 import BeautifulSoup

# Función para realizar una búsqueda en un motor de búsqueda específico
def buscar_en_motor_de_busqueda(consulta, motor="google", num_resultados=5):
    if motor == "google":
        # Realiza la búsqueda en Google
        url = f"https://www.google.com/search?q={consulta}&num={num_resultados}"
    elif motor == "bing":
        # Realiza la búsqueda en Bing
        url = f"https://www.bing.com/search?q={consulta}&count={num_resultados}"
    elif motor == "duckduckgo":
        # Realiza la búsqueda en DuckDuckGo
        url = f"https://duckduckgo.com/html/?q={consulta}&t=h_&ia=web"
    else:
        return []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Obtén los resultados (URLs) de la página de resultados del motor de búsqueda
    resultados = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith("http"):
            resultados.append(href)
    
    return resultados

# Ejemplo de búsqueda en varios motores de búsqueda
consulta = "Que es seo?"
urls_google = buscar_en_motor_de_busqueda(consulta, motor="google", num_resultados=5)
urls_bing = buscar_en_motor_de_busqueda(consulta, motor="bing", num_resultados=5)
urls_duckduckgo = buscar_en_motor_de_busqueda(consulta, motor="duckduckgo", num_resultados=5)

# Imprime las URLs de cada motor de búsqueda
print("URLs de Google:")
for url in urls_google:
    print(url)

print("\nURLs de Bing:")
for url in urls_bing:
    print(url)

print("\nURLs de DuckDuckGo:")
for url in urls_duckduckgo:
    print(url)
