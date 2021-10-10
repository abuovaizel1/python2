import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://coinmarketcap.com/currencies/cardano/')
soup = bs(res.text, "html.parser")
print(soup.prettify())

