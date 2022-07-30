# requests 모듈 사용법 공부
참조 : [https://me2nuk.com/Python-requests-module-example/](https://me2nuk.com/Python-requests-module-example/)

# requests 모듈

- python 사용자들을 위해 만들어진, 간단한 Python용 HTTP 라이브러리
- HTTP, HTTPS 웹 사이트에 요청하기 위해 자주 사용되는 모듈
- Crawling 과정에서 requests 모듈을 이용해 웹 사이트의 소스코드를 가져온 다음 파싱한다.
- **requests 코드 예시를 위해 [httpbin](http://httpbin.org/), [example](https://example.com/), [google](https://www.google.com/) 3개의 사이트를 이용**
    
    

# requests module FIle 구조

```markdown
requests/
	__version__.py
	_internal_utils.py
	adapters.py
	api.py
	auth.py
	certs.py
	compat.py
	cookies.py
	exceptions.py
	help.py
	hooks.py
	models.py
	mackages.py
	sessions.py
	status_codes.py
	structures.py
	utils.py
```

# requests model install

## 1. requests 설치

1. 터미널 열기
2. python 위치로 접근
3. `$ python -m pip install requests`

## 2. Source 코드 받기

- requests는 코드를 항상 사용할 수 있는 GitHub에서 개발됨.
- 첫번째:  `$ git clone git://github.com/psf/requests.git`
- 두번째 : `$ curl -OL https://github.com/psf/requests.git`

---

# requests Example Code

- **[https://example.com](https://example.com) URL에 요청한 다음 반환되는 값을 출력하는 코드**

```python
import requests
r = requests.get('https://example.com/')
r.status_code
# 200

r.text
'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title[ ... ]\n</body>\n</html>\n'
```

---

# HTTP 요청 메서드

- 클라이언트가 서버에 요청하는 목적과  그 종류를 알리는 수단
- 요청메서드에 따라 응답하는 방식 또한 다르며 다양한 메서드 존재
- 대표 메서드 : GET, POST 방식

---

# requests GET, POST, PUT, DELETE, HEAD, OPTIONS

- 메서드마다 함수와 매개변수가 각각 다름
- 일반적으로는 함수명만 변경하며 쉽게 가능
- 엑세스 방식 7가지
    
    ```python
    r = requests.get("http://httpbin.org/get")
    print(r)
    # <Response [200]>
    r = requests.post("http://httpbin.org/post")
    r = requests.put("http://httpbin.org/put")
    r = requests.head("http://httpbin.org/get")
    r = requests.patch("http://httpbin.org/patch")
    r = requests.delete("http://httpbin.org/delete")
    r = requests.options("http://httpbin.org/get")
    ```
    

---

# requests 모듈 사용법

# 1. Request

- `requests.request(method, url, **kwargs)`
- 요청의 모든 기능은 7가지 방법으로 액세스할 수 있습니다.

## 1.1 Request Headers

- 기본값으로 header 4개 포함

```python
r = requests.get('https://example.com')
r.request.headers
# {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
```

## 1.2 Request method

- requests 클래스에서 지원하는 요청 메서드를 쉽게 사용하기 위해서 총 7가지의 메소드를 이용하여 활용할 수 있어야 함
- HTTP/1.1 버전의 경우 여러가지의 메소드가 존재
    - PUT, GET, POST, HEAD, PATCH, DELETE, OPTIONS
    - 위의 7가지 메소드는 전부 `requests.request` 를 반환함
    
    ```python
    request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)
    ```
    
    - requests.get Function code
    
    ```python
    def get(url, params=None, **kwargs):
        [...]
        kwargs.setdefault('allow_redirects', True)
        return request('get', url, params=params, **kwargs)
    ```
    

### parameter

- url : 매개변수는 request객체에  사용되기 위한 url
- params : 튜플, 딕셔너리 형힉으로 매개변수에 넣으면 양식이 url로 인코딩되어 url에 추가됨
- data : 튜플, 딕셔너리 형식으로 매개변수에 넣으면 양식이 인코딩되어 요청 본문에 추가됨
- json : json 매개변수를 이용하여 요청 본문에 json 형식으로 추가됨
- **kwargs : 요청하기 위한 매개변수이며 `requests.sessions.Session.request`로 반환

<details>

<summary></summary>

<div markdown=’1’>

### 1.2.1 PUT

- `requests.put(url, data=None, **kwargs)`
    
    ```python
    def put(url, data=None, **kwargs):
        [...]
        return request('put', url, data=data, **kwargs)
    ```
    

### 1.2.2 GET

- `requests.get(url, params=None, **kwargs)`
    
    ```python
    def get(url, params=None, **kwargs):
        [...]
        kwargs.setdefault('allow_redirects', True)
        return request('get', url, params=params, **kwargs)
    ```
    

### 1.2.3 POST

- `requests.post(url, data=None, json=None, **kwargs)`
- data, json 두 개의 매개변수는 비슷해보이지만 요청할 때 헤더의 content-type이 달라짐
    
    ```python
    def post(url, data=None, json=None, **kwargs):
        [...]
        return request('post', url, data=data, json=json, **kwargs)
    ```
    

### 1.2.4 HEAD

- `requests.head(url, **kwargs)`
    
    ```python
    def head(url, **kwargs):
        [...]
        kwargs.setdefault('allow_redirects', False)
        return request('head', url, **kwargs)
    ```
    

### 1.2.5 PATCH

- `requests.patch(url, data=None, **kwargs)`
    
    ```python
    def patch(url, data=None, **kwargs):
        [...]
        return request('patch', url, data=data, **kwargs)
    ```
    

### 1.2.6 DELETE

- `requests.delete(url, **kwargs)`
    
    ```python
    def delete(url, **kwargs):
        [...]
        return request('delete', url, **kwargs)
    ```
    

### 1.2.7 OPTIONS

- `requests.options(url, **kwargs)`
    
    ```python
    def options(url, **kwargs):
        [...]
        kwargs.setdefault('allow_redircts', True)
        return request('options', url, **kwargs)
    ```
    

</div>

</details>

## 1.3. `requests.request`

```python
# 그래서 이렇게도 가능
methods = ['GET','POST']
r = requests.request(methods[0], 'http://httpbin.org/get', params={'test':'GET'})
r = requests.request(methods[1], 'http://httpbin.org/post', data={'test':'POST'}
```

## 1.4. request **kwargs

### `**kwargs`  종류

- **`request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)`**

<details>

<summary></summary>

<div markdown=’1’>

### 1.4.1 method(str)

- 요청 시 사용될 http 메소드(’GET’, ‘POST’, ‘PUT’ …)
    
    ```python
    r = requests.request(method = 'GET', url = '...')
    ```
    

### 1.4.2 url(str)

- <mark> core code </mark>
- 요청하고 싶은 url 넣기
    
    ```python
    r = requests.request('GET', url = 'https://example.com')
    ```
    

### 1.4.3 params(str, dict)

- <mark> core code </mark>
- 요청하는 url 뒤에 GET방식으로 파라미터가 붙음
    
    ```python
    r = requests.request('GET', url='https://example.com', params={'get1':'value1', 'get2':'value2'})
    print(r.url)
    # 'https://example.com?get=value1&get2=value2'
    ```
    

### 1.4.4 data(str, dict)

- <mark> core code </mark>
- 요청될 때 본문에 포함되어 서버로 데이터를 전송
    
    ```python
    r = requests.request('POST', url='http://httpbin.org/post', data={'post1':'value1', 'post2':'value2'})
    print(r.request.body)
    
    # 'post1=value1&post2=value2'
    
    r = requests.request('POST', url='http://httpbin.org/post', data='hello post data')
    print(r.request.body)
    
    # 'hello post data'
    ```
    

### 1.4.5 headers(dict)

- <mark> core code </mark>
- 요청할 때 기본적인 헤더에 추가/수정/편집하여 서버에 전송
    
    ```python
    from requests import request
    
    r = request('GET'. url='...', headers={'header_test':'test'})
    r.request.headers
    # {'User-Agent': 'python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'header_test': 'test'}
    print(r.request.headers['header_test']
    ```
    

### 1.4.6 cookies(dict)

- <mark> core code </mark>
- 헤더에 쿠키에 대한 정보를 포함시킴
    
    ```python
    from requests import request
    r = request('GET', url='https//example.com', cookies={'cookies1':'value1'})
    print(r.request._cookies)
    # <RequestsCookieJar[Cookie(version=0, name='cookies1', value='value1', port=None, port_specified=False, domain='', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)  ]>
    
    print(r.request._cookies.get_dict())
    {'cookies1':'value1'}
    ```
    

### 1.4.7 files(dict, List, tuple)

- <mark> core code </mark>
- 요청할 때 본문에 파일 내용을 포함시켜 파일 업로드하는 기능으로 사용할 수 있습니다.
- 파일 업로드를 위해 로컬에서 환경 구축한 다음 files매개변수를 이용하여 업로드할 수 있습니다.
    
    ```python
    from flask import Flask, request
    from werkzeug.utils import secure_filename
    
    app = Flask(__name__)
    
    @app.route('/uploads', method['POST']
    def FILE_Uploads():
        FILE = request.files('file')
        FILE.save(os.path.join('uploads/', secure_filename(FILE.filename)))
        
        return 'FILE Uploads Save'
    
    app.run('127.0.0.1', 8080)
    ```
    
    ```python
    from requests import request
    files = {'file':open('test.txt', 'rb')}
    url = 'http://127.0.0.1:8080/uploads'
    r = request('POST', url = url, files=files)
    print(r.request.body)
    
    # b'--97d3077d15f7c7f9fc153b18d4575e58\r\nContent-Disposition: form-data; name="flie"; filename="test.txt"\r\n\r\nFILE Uploads TEST!!\n\r\n--97d3077d15f7c7f9fc153b18d4575e58--\r\n'
    
    print(r.request.body.decode())
    --97d3077d15f7c7f9fc153b18d4575e58
      Content-Disposition: form-data; name="flie"; filename="test.txt"
    
      FILE Uploads TEST!!
    
    --97d3077d15f7c7f9fc153b18d4575e58--
    ```
    
    - content-type 지정 `(Filename, File Content, File conten Type)`
        
        ```python
        import requests
        files = {'files':('filename', 'file content', 'content-type')}
        r = requests.post("http://httpbin.org/post", files=files)
        print(r.json())
        # {'args': {}, 'data': '', 'files': {'files': 'file content'}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '185', 'Content-Type': 'multipart/form-data;    boundary=2dddfaca24abc6196d17482a29880613', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-6197c5ce-14e0abef60bf13d62a2d9f36'}, 'json': None, 'origin': '112.154.52.33',    'url': 'http://httpbin.org/post'}
        print(r.request.body.decode())
        '''
          --2dddfaca24abc6196d17482a29880613
          Content-Disposition: form-data; name="files"; filename="filename"
          Content-Type: content-type
        
          file content
          --2dddfaca24abc6196d17482a29880613--
        '''
         
        files = {'files':('test.html', open('test.html', 'rb'), 'text/html')}
        r = requests.post("http://httpbin.org/post", files=files)
        print(r.request.body.decode())
        '''
          --3cc6772156f774d6c834d9751d35ef44
          Content-Disposition: form-data; name="files"; filename="test.html"
          Content-Type: text/html
        
          <h1>html</h1>
        
          --3cc6772156f774d6c834d9751d35ef44--
        '''
        ```
        
    - 다중 파일 업로드
        
        ```python
        files = {'files1':open('test1.txt','rb'), 'files2':open('test2.txt'.'rb')}
        r = requests.post('http://httpbin.org/post", files=files)\
        ```
        
    

### 1.4.8 auth(tuple, list)

- <mark>core code</mark>
- authorization 헤더를 생성시켜 사용자 에이전트임을 증명할 수 있음
- authorization 헤더가 필요한 웹 사이트의 경우 auth를 이용하여 `Basic<base64>`형식으로 변환시켜 요청
    
    ```python
    r = requests.get('https://example.com', auth=('admin','pass'))
    print(r.request.headers['Authorization'])
    # 'Basic YWRtaW46cGFzcw=='
    ```
    

</div> 

</details>