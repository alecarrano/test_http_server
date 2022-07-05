#!/usr/bin/env python3

import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging
import time
import sys
import os

PORT = 8000

class GetHandler(
        SimpleHTTPServer.SimpleHTTPRequestHandler
        ):

    def do_GET(self):
        logging.error(self.headers)
        logging.error(os.environ.get('HOME', '/home/username/'))
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        logging.error(os.environ.get('HOME', '/home/username/'))
    
    def do_HEAD(self):
        sys.exit(1)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print("Serving on port d :8000")
httpd.serve_forever()
