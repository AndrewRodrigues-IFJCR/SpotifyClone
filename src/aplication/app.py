
class App: 
    name: str
    debug: bool

# Basics
def loadApp(app: App, **data: dict) -> App:
    app.name = data['name']
    app.debug = data['debug']
    return app

def dumpApp(app: App) -> dict:
    return {
        'name': app.name,
        'debug': app.debug
    }
