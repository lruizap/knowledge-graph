import shutil
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid_url(url, base_domain):
    # Comprobar si la URL pertenece al mismo dominio y si es un enlace válido
    parsed_url = urlparse(url)
    return bool(parsed_url.netloc) and parsed_url.netloc == base_domain and parsed_url.scheme in ['http', 'https']


def scrape_url(url, depth, max_depth, base_domain, visited, linksJina):
    if depth > max_depth:
        return
    try:
        response = requests.get(url)
        response.raise_for_status()  # Asegurar que la respuesta fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            full_link = urljoin(url, link['href'])
            if full_link not in visited and is_valid_url(full_link, base_domain):
                visited.add(full_link)
                linksJina.add("https://r.jina.ai/" + full_link)
                # Imprime el enlace actual
                print(f"Nivel {depth}: {full_link}")
                scrape_url(full_link, depth + 1, max_depth,
                           base_domain, visited, linksJina)
    except requests.RequestException as e:
        print(f"No se pudo acceder a {url} debido a {e}")


def main():
    # URL de inicio
    url = "https://www.elmundo.es/especiales/2009/09/internacional/segunda_guerra_mundial/armas/index.html/"
    # Parámetros de la búsqueda (profundidad máxima, dominio base, conjunto de enlaces visitados)
    max_depth = 1
    base_domain = urlparse(url).netloc
    visited = set()
    linksJina = set()

    print(f"Scrapeando {url}")
    scrape_url(url, 1, max_depth, base_domain, visited, linksJina)

    # Imprimir total de links
    print(f"Total de links: {len(visited)}")

    # Guardar linksJina en un archivo txt
    with open("linksJina.txt", "w", encoding="utf-8") as file:
        for link in linksJina:
            try:
                file.write(f"{link}\n")
            except:
                print(e)
                continue

    # Por cada link en visited, obtener la respuesta y guardarla en un archivo
    id = 0

    # Verificar si la carpeta 'responses' existe
    if os.path.exists("responses"):
        # Eliminar todos los archivos dentro de la carpeta 'responses'
        for filename in os.listdir("responses"):
            file_path = os.path.join("responses", filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"No se pudo eliminar {file_path}: {e}")
    else:
        # Si la carpeta 'responses' no existe, crearla
        os.makedirs("responses")

    # Ahora puedes guardar los archivos dentro de la carpeta 'responses'
    for id, link in enumerate(linksJina):
        print(f"Convirtiendo y almacenando {link}")
        response = requests.get(link)
        response.raise_for_status()
        # Guardar respuesta en un archivo dentro de la carpeta 'responses'
        with open(f"responses/response{id}.md", "w", encoding="utf-8") as file:
            file.write(response.text)


if __name__ == "__main__":
    main()
