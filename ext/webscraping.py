from bs4 import BeautifulSoup
import requests


def scraping(source):
    return BeautifulSoup(requests.get(source).content, "html.parser")

def lacraiatorrent():
    data = [
        {'name':'Teles of the Walking Dead', 'season':'s01', 'link':'https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'},
        {'name':'Titans', 'season':'s04', 'link':'https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/'},
        {'name':'Fear in the Walking Dead', 'season':'s08', 'link':'https://lacraiatorrent.com/fear-the-walking-dead-8-temporada-torrent-dublada/'},
        {'name':'The Rings of Power', 'season':'s02', 'link':'https://lacraiatorrent.com/o-senhor-dos-aneis-os-aneis-de-poder-2-temporada-torrent-dublada/'},
        {'name':'House of the Dragon', 'season':'s02', 'link':'https://lacraiatorrent.com/a-casa-do-dragao-2-temporada-torrent-dublada/'},
        {'name':'Succession', 'season':'s04', 'link':'https://lacraiatorrent.com/succession-4-temporada-torrent-dublada/'},
        {'name':'Barbarians', 'season':'s03', 'link':'https://lacraiatorrent.com/barbaros-3-temporada-completa-torrent-dublada/'},
        {'name':'Arcanjo Renegado', 'season':'s03', 'link':'https://lacraiatorrent.com/arcanjo-renegado-3-temporada-torrent/'},
        {'name':'She Hulk', 'season':'s02', 'link':'https://lacraiatorrent.com/mulher-hulk-defensora-de-herois-2-temporada-torrent-dublada/'},
        {'name':'Sandman', 'season':'s02', 'link':'https://lacraiatorrent.com/sandman-2-temporada-completa-torrent-dublada/'},
        {'name':'See', 'season':'s04', 'link':'https://lacraiatorrent.com/pagina-nao-encontrada-torrent/'}
    ]

    series = list()
    for i in data:
        try:
            series.append(f"{i['name']} {i['season']} {scraping(i['link']).find_all('span', class_='botao_dublado')[-1].text}")
        except:
            series.append(f"{i['name']} {i['season']} 'Aguardando dublagem'")
    return series

def init_api():
    result = lacraiatorrent()
    return result
