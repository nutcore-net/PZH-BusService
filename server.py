#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gzip, json
from urllib import request
from http.server import BaseHTTPRequestHandler, HTTPServer

constConf = {'servAdd':'http://221.10.182.250:55555', 'locAdd':'127.0.0.1', 'locPort':5555}
contentHTML = ''

class BusService(BaseHTTPRequestHandler):
    server_version = "BusService/1.0"
    
    def do_GET(self):
        allowAddr = ['/', '/favicon.ico','/BusService/Query_ByRouteID/','/BusService/Require_AllRouteData/','/BusService/Require_RouteStatData/']
 
        self.close_connection = True
        fname=self.path.split('?')[0]
        if fname in allowAddr:
            if fname is '/':
                self._sendHttpHeader(200,'text/html')
                self._sendHttpBody(contentHTML)
            elif fname is '/favicon.ico':
                self._sendHttpHeader(200,'application/x-ico')
                with open('favicon.ico','rb') as f:
                    self._sendHttpBody(f.read())
            else:
                self._sendHttpHeader(200)
                with request.urlopen(constConf['servAdd']+self.path) as f:
                    self._sendHttpBody(f.read())
        else:
            self._sendHttpHeader(404)
            self._sendHttpBody({'msg':'Not Found'})

    def do_POST(self):
        self.close_connection = True
        self.send_response(403)
        self.end_headers()
        self.wfile.write(b'Not Allowed')

    def _sendHttpHeader(self, code, contentType='application/json'):
        self.send_response(code)
        self.send_header('Content-Type', contentType)
        self.send_header('Content-Encoding','gzip')
        self.end_headers()

    def _sendHttpBody(self, data):
        body = b''
        if isinstance(data, bytes):
            body = data
        elif isinstance(data, str):
            body = data.encode('utf-8', errors='ignore')
        else:
            body = json.dumps(data).encode('utf-8', errors='ignore')
        self.wfile.write(gzip.compress(body))

def main():
    global contentHTML
    with open('index.html','r',encoding='utf-8') as f:
        contentHTML = f.read()
    contentHTML = contentHTML.replace('{ADDR}',constConf['locAdd']).replace('{PORT}',str(constConf['locPort']))
    httpd = HTTPServer((constConf['locAdd'], constConf['locPort']), BusService)
    print('Started BusService At %s:%s' % (constConf['locAdd'], constConf['locPort']))
    httpd.serve_forever()

if __name__ == '__main__':
    main()
