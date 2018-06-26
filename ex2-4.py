
#http.client.HttpConnection을 사용한 Get 방식 요청

from http.client import HTTPConnection


conn = HTTPConnection('www.example.com') #생성자 생성, 도메인입력
conn.request('GET', '/')  #방식,경로 입력
#conn.rquest('GET', '/board/list') #not found

r = conn.getresponse() #result 받기
print(r.status, r.reason)

data = r.read()
