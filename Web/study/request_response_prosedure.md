# 파이썬에서 요청(requests)과 응답(response)

```python
params = {
        'api_key' : '2ff4bcc7a40b2948d104065ad52b9329',
        'language' : 'ko-KR',
        'page' : '1',
    }
URL = 'https://api.themoviedb.org/3/movie/popular'
r = requests.get(URL, params=params)
# r의 타입은 <class 'requests.models.Response'>
print(r.text)
# r.text 타입은 str
print(r.json())
# r.json() 타입은 dict

```

### 파이썬에서 요청과 응답 구동 순서

1. 기본적으로 서버에 요청을 보내면 서버에서는 데이터를 데이터포맷인 HTML, JSON, xml 등의 다양한 형태로 전송한다.
2. 그 때 API docs를 확인해서 전송되는 응답의 형태를 확인해야 한다.
3. TMDB의 경우, TMDB API docs에서 RESPONSE 형태를 확인한다.
4. RESPONSES application/<Json, html, xml 등> 중 하나
5. JSON인 경우 응답은 문자열 형태로 응답이 전해진다.
6. 응답받자마자 읽을 수 있는 자료는 text라는 인스턴스 변수에 저장한다.
    - text엔  requests.get().encoding으로 디코드 되었다.
    - 문서의 인코딩 방식을 자동적으로 추측하고 그에 맞게 디코딩해준다는 점에서 굉장히 편리함
    
7. 이러한 json 데이터를 딕셔너리형태로 가공할 수 있도록 자료형을 바꿔주는 함수가 requests.get().json()이다.

### json(Javascript Object Notation)

- 응답할 때 데이터를 보낼 때 사용하는 개방형 표준 포맷으로, 클라이언트가 사용하는 언어에 관계없이 통일된 데이터로 주고받을 수 있도록 일정한 패턴을 지닌 문자열을 생성해 내보내면 클라이언트는 이를 해석해 데이터를 자기만의 방식으로 온전히 저장, 표시할 수 있게 됨
- 속성-값 쌍으로 이뤄진 데이터 오프젝트 형태로 전달됨(js에서 object는 파이썬에서 dictionary를 의미한다.)
- 비동기 통신을 위해 AJAX에서 많이 사용됨
- 문자열을 전송받은 후에 해당 문자열을 바로 파싱(XML보다 빠른 처리속도)
- HTML과 자바스크립트가 연동되어 빠른 응답이 필요한 웹 환경에서 많이 사용됨
- XML을 대체하는 주요 데이터 포맷

### r.text :

- HTTP request를 보낸 URL에서 readable한 내용을 가져올 때 사용
- r.text를 사용하는 경우에 r.encoding이라는 리소스를 사용할 수 있음.
    - requests 모듈 자체에서 request를 바탕으로 받은 response를 자동으로 encoding을 추측하고 해당 인코딩 값으로 디코드 시킨 값이 r.text이다.
    - 그러면.. response가 json형식일 때 이를 모듈 내에서 json 형태를 추측하고 해당값에 맞게 디코딩 시켜놓으면 어떤 형태로 str타입으로 text에 저장되는 것?

### r.content

- r.text와의 차이점은 디코딩되지 않았다는 점
- HTTP response의 body 부분이 bytes상태로 그대로 저장되어 있음
- 이미지 등의 미디어 파일을 다른 서버로부터 받고 싶을 때는 r.content를 사용해야 한다.