from bs4 import BeautifulSoup
import requests


def scraping(link):
    return BeautifulSoup(requests.get(link).content, "html.parser")

def lacraiatorrent():
    data = [
        web(id=1, name="Teles of the Walking Dead", season="s01", link="https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/"),
        web(id=2, name="Titans", season="s04", link="https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/"),
        web(id=3, name="Fear in the Walking Dead", season="s08", link="https://lacraiascraping.com/fear-the-walking-dead-8-temporada-torrent-dublada/"),
        web(id=4, name="The Rings of Power", season="s02", link="https://lacraiascraping.com/o-senhor-dos-aneis-os-aneis-de-poder-2-temporada-torrent-dublada/"),
        web(id=5, name="House of the Dragon", season="s02", link="https://lacraiascraping.com/a-casa-do-dragao-2-temporada-torrent-dublada/"),
        web(id=6, name="Succession", season="s04", link="https://lacraiascraping.com/succession-4-temporada-torrent-dublada/"),
        web(id=7, name="Barbarians", season="s03", link="https://lacraiascraping.com/barbaros-3-temporada-completa-torrent-dublada/"),
        web(id=8, name="Arcanjo Renegado", season="s03", link="https://lacraiascraping.com/arcanjo-renegado-3-temporada-torrent/"),
        web(id=9, name="She Hulk", season="s02", link="https://lacraiascraping.com/mulher-hulk-defensora-de-herois-2-temporada-torrent-dublada/"),
        web(id=10, name="Sandman", season="s02", link="https://lacraiascraping.com/sandman-2-temporada-completa-torrent-dublada/")
    ]
    return data

def init_api(links):
    for link in links:
        series = scraping(link).find_all("span", class_="botao_dublado")[-1].text
    print(series)
    return series
