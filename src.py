from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://coinmarketcap.com/currencies/cardano/"

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')


def getRequest(currName):
    some_list = []
    for paragraph in soup.find_all("p"):
        if currName in paragraph.get_text():
            some_list.append(paragraph.get_text())
    return some_list


def gettingData():
    some_list = []
    for paragraph in soup.find_all("p"):
        some_list.append(paragraph.get_text())
    return some_list
