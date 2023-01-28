from ext.database import base, engine, session
from models import website


def populateDb():
    base.metadata.drop_all(engine)

    base.metadata.create_all(engine)

    session.add_all([
        website(author='https://lacraiatorrent.com/tales-of-the-walking-dead-1-temporada-legendada-torrent/'),
        website(author='https://lacraiatorrent.com/titas-4-temporada-legendada-torrent/'),
        website(author='https://lacraiatorrent.com/fear-the-walking-dead-7-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/o-senhor-dos-aneis-os-aneis-de-poder-1-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/a-casa-do-dragao-1-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/succession-3-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/barbaros-2-temporada-completa-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/arcanjo-renegado-2-temporada-torrent/'),
        website(author='https://lacraiatorrent.com/mulher-hulk-defensora-de-herois-1-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/sandman-1-temporada-completa-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/see-3-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/manifest-o-misterio-do-voo-828-4-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/the-last-of-us-1-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/vikings-valhalla-2-temporada-torrent-dublada/'),
        website(author='https://lacraiatorrent.com/jack-ryan-completa-torrent-dublada/')
    ])

    session.commit()
