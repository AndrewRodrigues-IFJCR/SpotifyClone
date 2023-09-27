
class Style:
    name: str

def loadStyle(style: Style, **data: dict) -> Style:
    style.name = data['name']
    return style

def dumpStyle(style: Style) -> dict:
    return {
        'name': style.name
    }