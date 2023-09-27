
class Route:
    get: bool
    post: bool
    endpoint: str

def loadRoute(route: Route, **data: dict) -> Route:
    route.get = data['get']
    route.post = data['post']
    route.endpoint = data['endpoint']
    return route

def dumpRoute(route: Route) -> dict:
    return {
        'get': route.get,
        'post': route.post,
        'endpoint': route.endpoint
    }
