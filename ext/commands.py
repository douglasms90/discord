from ext.webscraping import website


def lacraiatorrent():
    data = [
        dict(name='Teles of the Walking Dead', link='https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'),
        dict(name='Titans', link='https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/'),
        dict(name='Fear in the Walking Dead', link='https://lacraiatorrent.com/fear-the-walking-dead-8-temporada-torrent-dublada/'),
        dict(name='The Rings of Power', link='https://lacraiatorrent.com/o-senhor-dos-aneis-os-aneis-de-poder-2-temporada-torrent-dublada/'),
        dict(name='House of the Dragon', link='https://lacraiatorrent.com/a-casa-do-dragao-2-temporada-torrent-dublada/'),
        dict(name='Succession', link='https://lacraiatorrent.com/succession-4-temporada-torrent-dublada/'),
        dict(name='Barbarians', link='https://lacraiatorrent.com/barbaros-3-temporada-completa-torrent-dublada/'),
        dict(name='Arcanjo Renegado', link='https://lacraiatorrent.com/arcanjo-renegado-3-temporada-torrent/'),
        dict(name='She Hulk', link='https://lacraiatorrent.com/mulher-hulk-defensora-de-herois-2-temporada-torrent-dublada/'),
        dict(name='Sandman', link='https://lacraiatorrent.com/sandman-2-temporada-completa-torrent-dublada/'),
        dict(name='See', link='https://lacraiatorrent.com/pagina-nao-encontrada-torrent/')
    ]

    series = list()
    for i in data:
        try:
            series.append(f"**{i['name']}** {website(i['link']).find_all('span', class_='botao_dublado')[-1].text}")
        except:
            series.append(f"**{i['name']}** Aguardando dublagem")
    return series

def init_api():
    result = lacraiatorrent()
    return result
