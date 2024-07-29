import requests
from bs4 import BeautifulSoup

def extract_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    for product in soup.find_all('div', class_='product'):
        name = product.find('h2').text
        price = product.find('span', class_='price').text
        availability = product.find('span', class_='availability').text
        products.append({'name': name, 'price': price, 'availability': availability})
    
    return products

