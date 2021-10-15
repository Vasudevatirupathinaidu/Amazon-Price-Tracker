import requests
from bs4 import BeautifulSoup

def get_link_data(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept-Language": "en",}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    name = soup.find(id="productTitle").text.strip()
    try:
        price = soup.select_one("span.offer-price").text.strip()[1:]
    except AttributeError:
        price = soup.select_one("span[id *= 'priceblock']").text.strip()[1:]
    if ',' in price:
        price = float(price.replace(',',''))
    price = float(price)
    
    return name, price
