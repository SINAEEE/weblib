
from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9000
class MyHttpReqeustHandler(BaseHTTPRequestHandler):
#웹서버 응답핸들러
#정해진 포트로 request가 들어온 경우 그에대한 응답을 돌려줌

    def do_GET(self): #GET 방식의 request만 처리
        self.send_response(200) #200코드 : request를 잘받았다는의미
        self.send_header('Content-Type','text/html:charset=utf-8')
        #response 헤더 추가 : 헤더를 추가해서 브라우저에 request를 전송한다고 알려줌
        print('receive request')
        self.end_headers() #response 헤더의 끝 추가
        self.wfile.write('<h5>Hello World</h5>'.encode('utf-8')) #html소스자체를 출력



#서버 구동
httpd = HTTPServer(('',9000),MyHttpReqeustHandler)
print('HTTP server starts....')
httpd.serve_forever()