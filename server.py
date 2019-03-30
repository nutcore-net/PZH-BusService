#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gzip, json
from urllib import request
from http.server import BaseHTTPRequestHandler, HTTPServer

conf = {
    'servAddr':'http://221.10.182.250:55555',
    'pubAddr':'http://127.0.0.1:5555',
    'bindPort':5555
}

allowAddr = [
    '/BusService/Query_ByRouteID/',
    '/BusService/Require_AllRouteData/',
    '/BusService/Require_RouteStatData/'
]

HTML = b''
ICON = b''

class BusService(BaseHTTPRequestHandler):
    server_version = 'BusService/1.0'
    sys_version = ''
    
    def do_GET(self):
        fname=self.path.split('?')[0]
        if fname == '/':
            self._sendHttpHeader(200, 'text/html')
            self._sendHttpBody(HTML)
        elif fname == '/favicon.ico':
            self._sendHttpHeader(200, 'application/x-ico')
            self._sendHttpBody(ICON)
        elif fname in allowAddr:
            self._sendHttpHeader(200, 'application/json')
            with request.urlopen(conf['servAddr']+self.path) as f:
                self._sendHttpBody(f.read())
        else:
            self._sendHttpHeader(404)
            self._sendHttpBody(b'404 Not Found')

    def do_POST(self):
        self._sendHttpHeader(403)
        self._sendHttpBody(b'403 Forbidden')

    def _sendHttpHeader(self, code, contentType='text/plain'):
        self.close_connection = True
        self.send_response(code)
        self.send_header('Content-Type', contentType)
        self.end_headers()

    def _sendHttpBody(self, data):
        self.wfile.write(data)

def main():
    global HTML, ICON

    with open('index.html','r',encoding='utf-8') as f:
        HTML = f.read().replace('{ADDR}',conf['pubAddr']).encode('utf-8')

    with open('favicon.ico','rb') as f:
        ICON = f.read()
    
    print('Started BusService.')

    httpd = HTTPServer(('', conf['bindPort']), BusService)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
