

#http.client.HttpConnection을 사용한 HEAD방식 요청

from http.client import HTTPConnection


conn = HTTPConnection('www.example.com') #생성자 생성, 도메인입력
conn.request('HEAD', '/')  #방식,경로 입력

r = conn.getresponse() #result 받기
print(r.status, r.reason)

data = r.read()
print(data)
