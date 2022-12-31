from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

from bs4 import BeautifulSoup
import requests


def website(source):
    return BeautifulSoup(requests.get(source).content, "html.parser")


base = declarative_base()

class Web(base):
    __tablename__ = 'web'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    link = Column(String(200))

engine = create_engine('sqlite:///development.db', echo=True)

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

session.add_all([
    Web(name='Teles of the Walking Dead', link='https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'),
    Web(name='Titans', link='https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/'),
    Web(name='Fear in the Walking Dead', link='https://lacraiatorrent.com/fear-the-walking-dead-8-temporada-torrent-dublada/'),
    Web(name='The Rings of Power', link='https://lacraiatorrent.com/o-senhor-dos-aneis-os-aneis-de-poder-2-temporada-torrent-dublada/'),
    Web(name='House of the Dragon', link='https://lacraiatorrent.com/a-casa-do-dragao-2-temporada-torrent-dublada/'),
    Web(name='Succession', link='https://lacraiatorrent.com/succession-4-temporada-torrent-dublada/'),
    Web(name='Barbarians', link='https://lacraiatorrent.com/barbaros-3-temporada-completa-torrent-dublada/'),
    Web(name='Arcanjo Renegado', link='https://lacraiatorrent.com/arcanjo-renegado-3-temporada-torrent/'),
    Web(name='She Hulk', link='https://lacraiatorrent.com/mulher-hulk-defensora-de-herois-2-temporada-torrent-dublada/'),
    Web(name='Sandman', link='https://lacraiatorrent.com/sandman-2-temporada-completa-torrent-dublada/'),
    Web(name='See', link='https://lacraiatorrent.com/pagina-nao-encontrada-torrent/')
])

session.commit()


series = list()
for scraping in session.query(Web).order_by(Web.id):
    try:
        series.append(f"{scraping.name} {website(scraping.link).find_all('span', class_='botao_dublado')[-1].text}")
    except:
        series.append(f"{scraping.name} 'Aguardando dublagem'")
print(series)
