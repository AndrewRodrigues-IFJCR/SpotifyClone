
class Band:
    name: str

def loadBand(band: Band, **data: dict) -> Band:
    band.name = data['name']
    return band

def dumpBand(band: Band) -> dict:
    return {
        'name': band.name
    }