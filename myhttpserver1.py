
from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9000
class MyHttpReqeustHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html:charset=utf-8')
        print('receive request')
        self.end_headers()
        self.wfile.write('<h5>Hello World</h5>'.encode('utf-8'))



#서버 구동
httpd = HTTPServer(('',9000),MyHttpReqeustHandler)
print('HTTP server starts....')
httpd.serve_forever()