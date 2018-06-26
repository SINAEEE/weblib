
from urllib.request import urlopen, Request
from urllib.parse import urlencode

data = urlencode({ 'a': 'Whatdoesthefoxsay', 'b': 'lingdingdingdingdingdiding' })
data = data.encode('UTF-8')
#urlparse()를 사용하여 쿼리스트링을 얻는것이 아닌 직접 쿼리스트링을 만들어 인코딩 하고 싶은 경우
#딕셔너리 또는 key와 value로 맵핑된 튜플을 가진 리스트를 넘겨 사용 가능

#urlencode : 쿼리스트링 파라미터를 Encoding

#print(data) : b'a=Whatdoesthefoxsay&b=lingdingdingdingdingdiding'

request = Request('http://www.example.com',data)
request.add_header('Content-Type', 'text/html')

f = urlopen(request)
print(f.read())
