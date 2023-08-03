import requests
from bs4 import BeautifulSoup

def scrape_ddtech():
    url = "https://ddtech.mx/productos/componentes/tarjetas-de-video"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("No se pudo acceder a la página.")

    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='product-info text-left')

    data = []
    for product in products:
        name = product.find('a', title=True).get('title')
         # Intentar obtener el precio dentro de la etiqueta label
        try:
            price = product.find('div', class_='clear').text.strip()
        except AttributeError:
            price = "Precio no disponible"
        data.append((name, price))

    return data

if __name__ == "__main__":
    scraped_data = scrape_ddtech()

    # Imprime la información en la terminal
    for name, price in scraped_data:
        print(f"Nombre: {name}")
        print(f"Precio: {price}")
        print("=" * 30)












