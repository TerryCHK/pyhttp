# Top level server object for responding to requests


from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    def __init__(self, router, *args, **kwargs):
        self.router = router
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """
        Definition of GET method
        """
        ret_code, ret_data = self.router.get_routes(self.path,"GET")()
        try:
            ret_code, ret_data = self.router.get_routes(self.path,"GET")()
        except:
            ret_code = 404
            ret_data = "Unsupported"
        self.send_response(ret_code)
        self.end_headers()
        self.wfile.write(bytes(ret_data, 'utf-8'))

    def do_PUT(self):
        """
        Definition of PUT method
        """
        try:
            content_length = int(self.headers['Content-Length'])
            encoded_body = self.rfile.read(content_length)
            body = encoded_body.decode('utf-8')
            ret_code, ret_data = self.router.get_routes(self.path,"PUT")(body)
        except:
            ret_code = 404
            ret_data = "Unsupported"
        self.send_response(ret_code)
        self.end_headers()
        self.wfile.write(bytes(ret_data, 'utf-8'))

    def do_POST(self):
        """
        Definition of POST method
        """
        ret_code = 404
        ret_data = "Unsupported"
        self.send_response(ret_code)
        self.end_headers()
        self.wfile.write(bytes(ret_data, 'utf-8'))

    def do_DELETE(self):
        """
        Definition of DELETE method
        """
        ret_code = 404
        ret_data = "Unsupported"
        self.send_response(ret_code)
        self.end_headers()
        self.wfile.write(bytes(ret_data, 'utf-8'))
