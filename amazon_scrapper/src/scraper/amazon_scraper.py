import requests
from bs4 import BeautifulSoup
from model.data_model import Product
from .utils import extract_text
from config import BASE_URL, HEADERS
import time
import random

class AmazonScraper:
    def scrape(self, query, pages=20):
        products = []
        for page in range(1, pages + 1):
            url = f"{BASE_URL}{query}&page={page}"
            print("URL:", url)

            for attempt in range(3): 
                response = requests.get(url, headers=HEADERS)
                if response.status_code == 200:
                    print("Response:", response.status_code)
                    delay = random.uniform(3, 7)
                    time.sleep(delay)
                    break    
                time.sleep(2 ** attempt)  

                print("Response:", response.status_code)

            if response.status_code != 200:
                print(f"Failed to fetch page {page} for query {query}.")
                continue

            soup = BeautifulSoup(response.content, 'html.parser')
            product_elements = soup.find_all("div", {"data-component-type": "s-search-result"})
            for element in product_elements:
                title_element = element.find("h2", {"class": "a-size-medium"})
                title = title_element["aria-label"] if title_element and "aria-label" in title_element.attrs else extract_text(element.find("span", class_="a-size-medium"))
                reviews = extract_text(element.find("span", class_="a-size-base"))
                price = extract_text(element.find("span", class_="a-offscreen"))
                image_url = element.find("img")['src'] if element.find("img") else None
                past_month_sales = extract_text(element.find("span", class_="a-size-base a-color-secondary"))


                product = Product(
                    title=title,
                    total_reviews=reviews,
                    price=price,
                    image_url=image_url,
                    past_month_sales=past_month_sales
                )
                products.append(product)

        return products
