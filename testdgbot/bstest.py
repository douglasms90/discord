from bs4 import BeautifulSoup
import requests

source = 'https://lacraiatorrent.com/the-last-of-us-1-temporada-hbo-completa-torrent-dublada/'

def soup(source):
    return BeautifulSoup(requests.get(source).content, "html.parser")

site = soup(source)
print(site.find_all('span', class_='info_dados')[0].text)
print(site.find_all('span', class_='botao_dublado')[-1].text)

