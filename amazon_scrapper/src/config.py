import random


HEADERS ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
BASE_URL = "https://www.amazon.com/s?k="


PROXIES = [
    'http://146.70.18.122:80',
]


PROXY = {'http': random.choice(PROXIES)}