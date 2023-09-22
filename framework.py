class Router:
    def __init__(self):
        self._routes = {}
        
    def bind(self, url, method, action):
        self._routes[(url, method)] = action
        
    def runRequest(self, url, method):
        return self._routes.get((url, method), lambda: "Error 404: Not Found")()