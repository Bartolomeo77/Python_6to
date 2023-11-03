from duckduckgo_search import DDGS

def obtener_urls_relevantes_ddg(consulta, num_resultados):
    with DDGS() as ddgs:
        urls = [r['href'] for r in ddgs.text(consulta, safesearch='off', max_results=num_resultados)]
    return urls

consulta = "que es seo?"
num_resultados = 5

# Obtener URLs relevantes de DuckDuckGo
urls_relevantes_ddg = obtener_urls_relevantes_ddg(consulta, num_resultados)
print(urls_relevantes_ddg)
