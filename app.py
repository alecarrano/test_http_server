#!/usr/bin/env python3

import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging
import time
import sys
import os
import psycopg2

PORT = 8000

class GetHandler(
        SimpleHTTPServer.SimpleHTTPRequestHandler
        ):

    def do_GET(self):
        logging.error(self.headers)
        logging.error(os.environ.get('PRINT_VAR', '/home/username/'))
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        conn = psycopg2.connect(
                database=os.environ.get('DB_DBNAME', 'f'), user=os.environ.get('DB_USER', 'f'), password=os.environ.get('DB_PASSWORD', 'f'), host=os.environ.get('DB_HOST', 'f'), port= os.environ.get('DB_PORT', 'f')
                )
        logging.error('connected')
        
    def do_POST(self):
        logging.error(self.headers)
        logging.error(os.environ.get('PRINT_VAR', '/home/username/'))
    
    def do_HEAD(self):
        sys.exit(1)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print("Serving on port d :8000")
httpd.serve_forever()
