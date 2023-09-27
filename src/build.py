from src.aplication.app import App, loadApp
from src.aplication.route import Route, loadRoute, dumpRoute
from src.aplication.framework.flask import FlaskFramework, initFlask, startFlask

# Alias
yes=True
no=False

app = loadApp(App, data={
    'name': 'Spotify Clone',
    'debug': yes
})

routes = {
    'user': [
        loadRoute(Route, data={
            'get': no,
            'post': no,
            'endpoint': '/api/authenticate/login'
        })
    ]
}

framework = initFlask(app, FlaskFramework)
startFlask(framework)
