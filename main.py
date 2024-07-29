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


url = 'https://mascotamoda.com//products' 
data = extract_product_data(url)
print(data)

import pandas as pd

def clean_transform_data(data):
    df = pd.DataFrame(data)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    df['availability'] = df['availability'].str.lower()
    return df

def analyze_data(df):
    summary = df.describe()
    return summary


df = clean_transform_data(data)
summary = analyze_data(df)
print(summary)

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def analyze_data_with_timer(df):
    return analyze_data(df)


summary = analyze_data_with_timer(df)
print(summary)

def extract_all_products(base_url, num_pages):
    all_products = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        try:
            products = extract_product_data(url)
            all_products.extend(products)
        except Exception as e:
            print(f"Error extracting data from page {page}: {e}")
    return all_products


base_url = 'https://mascotamoda.com//products'  
all_data = extract_all_products(base_url, 5)
print(all_data)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def read_from_csv(filename):
    return pd.read_csv(filename)


save_to_csv(df, 'products.csv')
df_from_file = read_from_csv('products.csv')
print(df_from_file)


from scraping.extract import extract_product_data
from analysis.transform import clean_transform_data
from analysis.analyze import analyze_data
from utils.file_io import save_to_csv, read_from_csv
from utils.decorators import timer_decorator

@timer_decorator
def main():
    base_url = 'https://mascotamoda.com//products'  
    data = extract_product_data(base_url)
    df = clean_transform_data(data)
    summary = analyze_data(df)
    save_to_csv(df, 'products.csv')
    print(summary)

if __name__ == "__main__":
    main()
