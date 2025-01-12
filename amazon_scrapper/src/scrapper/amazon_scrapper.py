import requests
from bs4 import BeautifulSoup
from .data_model import Product
from .utils import extract_text
from config import BASE_URL, HEADERS

class AmazonScraper:
    def scrape(self, query, pages=20):
        products = []
        for page in range(1, pages + 1):
            url = f"{BASE_URL}{query}&page={page}"
            response = requests.get(url, headers=HEADERS)
            if response.status_code != 200:
                print(f"Failed to fetch page {page} for query {query}.")
                continue

            soup = BeautifulSoup(response.content, 'html.parser')
            product_elements = soup.find_all("div", {"data-component-type": "s-search-result"})
            for element in product_elements:
                title = extract_text(element.find("span", class_="a-size-medium"))
                reviews = extract_text(element.find("span", class_="a-size-base"))
                price = extract_text(element.find("span", class_="a-offscreen"))
                image_url = element.find("img")['src'] if element.find("img") else None

                product = Product(
                    title=title,
                    total_reviews=reviews,
                    price=price,
                    image_url=image_url
                )
                products.append(product)

        return products
