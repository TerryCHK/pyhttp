#!/usr/bin/env python3


import signal
import inputs, router, server, sighand
from http.server import HTTPServer
from functools import partial


# Main loop
# - requires adding threading to serve concurrent requests
if __name__ == "__main__":
    signal.signal(signal.SIGINT, sighand.signal_handler)
    host = inputs.setup_host()
    inputs.show_server_info(host)
    handler = partial(server.Server, router.load_routes())
    httpd = HTTPServer(host, handler)
    httpd.serve_forever()
