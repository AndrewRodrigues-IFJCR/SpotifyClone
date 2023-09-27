from src.aplication.app import App
from flask import Flask

class FlaskFramework:
    app: App
    flask: Flask

def startFlask(framework: FlaskFramework) -> None: 
    framework.flask.run(debug=framework.app.debug)

def initFlask(app: App, framework: FlaskFramework) -> FlaskFramework: 
    framework.app = app
    framework.flask = Flask(framework.app.name)
    return framework
