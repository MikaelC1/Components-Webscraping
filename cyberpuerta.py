import requests
from bs4 import BeautifulSoup

def scrape_cyberpuerta():
    url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-de-Video/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("No se pudo acceder a la página.")

    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('a', class_='emproduct_right_title')

    data = []
    for product in products:
        name = product.text.strip()
        price = product.find_next('span', class_='price').text.strip()
        data.append((name, price))

    return data

if __name__ == "__main__":
    scraped_data = scrape_cyberpuerta()

    # Imprime la información en la terminal
    for name, price in scraped_data:
        print(f"Nombre: {name}")
        print(f"Precio: {price}")
        print("=" * 30)
