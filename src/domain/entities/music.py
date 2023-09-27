from src.entities.band import Band, loadBand, dumpBand
from src.entities.style import Style, loadStyle, dumpStyle

class Music:
    name: str
    band: Band
    style: Style

def loadMusic(music: Music, **data: dict) -> Music:
    music.name = data['name']
    music.band = loadBand(data['band'])
    music.style = loadStyle(data['style'])
    return music

def dumpMusic(music: Music) -> dict:
    return {
        'name': music.name,
        'band': dumpBand(music.band),
        'style': dumpStyle(music.style)
    }
