from ext.database import db, dbo, base, engine, session
from models import website


def populateDB():
    base.metadata.drop_all(engine)

    base.metadata.create_all(engine)

    session.add_all([
        website(name='Teles of the Walking Dead', link='https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'),
        website(name='Titans', link='https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/'),
        website(name='Fear in the Walking Dead', link='https://lacraiatorrent.com/fear-the-walking-dead-8-temporada-torrent-dublada/'),
        website(name='The Rings of Power', link='https://lacraiatorrent.com/o-senhor-dos-aneis-os-aneis-de-poder-2-temporada-torrent-dublada/'),
        website(name='House of the Dragon', link='https://lacraiatorrent.com/a-casa-do-dragao-2-temporada-torrent-dublada/'),
        website(name='Succession', link='https://lacraiatorrent.com/succession-4-temporada-torrent-dublada/'),
        website(name='Barbarians', link='https://lacraiatorrent.com/barbaros-3-temporada-completa-torrent-dublada/'),
        website(name='Arcanjo Renegado', link='https://lacraiatorrent.com/arcanjo-renegado-3-temporada-torrent/'),
        website(name='She Hulk', link='https://lacraiatorrent.com/mulher-hulk-defensora-de-herois-2-temporada-torrent-dublada/'),
        website(name='Sandman', link='https://lacraiatorrent.com/sandman-2-temporada-completa-torrent-dublada/'),
        website(name='See', link='https://lacraiatorrent.com/see-4-temporada-completa-torrent-dublada/'),
        website(name='Manifest', link='https://lacraiatorrent.com/manifest-o-misterio-do-voo-828-2-temporada-completa-torrent-dublada/'),
        website(name='The Last of Us', link='https://lacraiatorrent.com/the-last-of-us-1-temporada-torrent-dublada/')
    ])

    session.commit()
