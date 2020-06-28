# Router for managing server API endpoints
# Imports endpoint functionality from functions.py


import functions
from functools import partial


class Router:
    """
    Route format: {<path>: {<request_type>: <action>}}
    """
    def __init__(self):
        self.routes = {}

    def add_route(self, route):
        """
        Add route with defined action (function call)
        """
        new_route = {route["method"]: route["action"]}
        if route["path"] in self.routes:
            if not route["method"] in self.routes[route["path"]]:
                self.routes[route["path"]] = dict(self.routes[route["path"]], **new_route)
                return
            self.routes[route["path"]] = dict(self.routes[route["path"]], **{new_route})
        self.routes = dict(self.routes, **{route["path"]: new_route})

    def get_routes(self, path, method, data=None):
        return self.routes[path][method]

    def show_routes(self):
        """
        Return route table in string format
        """
        return str([route for route in self.routes])

def load_routes():
    router = Router()
    router.add_route({"path": "/", "method": "GET",
        "action": functions.get_example})
    router.add_route({"path": "/", "method": "PUT",
        "action": partial(functions.put_example, "put endpoint")})
    return router
