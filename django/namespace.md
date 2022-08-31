# Namespace

- 개체를 구분할 수 있는 범위를 나타냄

## - 필요성

- 문제 발생 1
    1. articles app index 페이지에 작성한 두번째 앱 index로 이동하는 하이퍼링크를 클릭 시 현재 페이지로 다시 이동 >> **URL namespace**
    2. page app의 index url(http://127.0.0.1:8000/pages/index/)로 직접 이동해도 aricles app의 index가 출력됨 >> **template namespace**

## - URL namespace

- url namespace를 사용하면 서로 다른 앱에서 동일한 url이름을 사용하는 경우에도 이름이 지정된 url을 고유하게 사용 가능
- **app_name :** attribute를 작성해 url namespace를 설정
    
    ```python
    
    # articles/urls.py
    
    app_name = 'articles'
    urlpatterns = [
       ...
    ]
    ```
    

- **URL 태그 변화**
    - `{% url 'index' %}` → `{% url 'articles:index' %}`
    - app_name을 지정한 후 url 태그에서는 반드시 app_name형태로만 사용해야 함
        - , or `raise NotReverceMatch` 에러
        
- URL 참조
    - ‘:’ 연산자를 사용하여 지정
        - 예 > `articles:index`
        

## - Template namespace

- Django는 기본적으로 app_name/templates/경로에 있는 templates파일들만 찾을 수 있음
- setting.py의 INSTALLED_APPS에 작성한 app순서로 template를 검색 후 렌더링함
- 해당 경로 활성화시키는 속성값
- 앱이 많아지면 같은 이름의 템플릿 파일이 존재하기 마련이기에 **template namespace 요구됨**
    
    ```python
    # settings.py
    TEMPLATES = [
        {
            ...
            'APP_DIRS':True,
            ...
        }
    ]
    ```
    

### - 디렉토리 생성을 통해 물리적인 이름 공간 구분

- 폴더 구조 변경
    - `app_name/templates/app_name/`
    - 기본 경로 자체를 변경할 수 없기 때문에 물리적으로 이름 공간 만들기

### - 탬플릿 경로 변경

- 폴더 구조 변경 후 경로로 해당되는 모든 부분 수정
    
    ```python
    # articles/views.py
    return render(request, 'articles/index.html')
    
    # pages/views.py
    return render(request, 'pages/index.html')
    ```
    

---