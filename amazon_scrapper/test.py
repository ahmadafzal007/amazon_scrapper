import requests
from bs4 import BeautifulSoup
import time
import random




url = "https://www.amazon.com/s?k=headphones&page=1"

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

html = requests.get(url, headers=headers)


print(html.status_code)