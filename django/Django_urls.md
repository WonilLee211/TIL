# 목차

- variable routing
- app url mapping
- naming url patterns

# variable routing

- url 주소를 변수로 사용하는 것을 의미
- 일부를 변수로 지정하여 view 함수 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path에 여러 페이지를 연결시킬 수 있음

## - 작성

- ‘<>’에 정의
- view함수의 인자로 할당
- 기본 타입 : string
    - 5가지 타입으로 명시할 수 있음
    1. srting
        - ‘/’를 제외하고 비어있지 않는 모든 문자열
        - 작성하지 않을 경우 기본 값
    2. int
        - 0 or 양의 정수와 매치
    3. slug
    4. uuid
    5. path
    
    ```python
    # urls.py
    
    urlpattern =[ 
        ...,
        # path('hello/<str:name>/', views.hello),
        path('hello/<name>/', views.hello),
    ]
    ```
    
- variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음
    
    ```python
    # articles/views.py
    
    def hello(request, name):
        context = {
            'name':name
        }
    
        return render(request, 'hello.html', context)
    ```
    
    ## 실습
    
    ```python
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        # variable routing 사용 시 주의점
        # 1. 변수명과 views.py의 매개변수의 이름이 같아야 한다.
        # 2. variable routing이 설정되면 반드시 매개변수로 받아야 한다.
        # 3. variable routing이 적용된 주조는 반드시 값이 입력되어야 한다.
        path('hello/<name>/<int:age>/', views.hello, name='hello')
    ]
    ```
    
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def hello(request, name, age):
        context = {
            'name':name,
            'age':age,
        }
        return render(request, 'articles/hello.html', context)
    ```
    
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
    <p>variable routing 예제</p>
    <h2>안녕하세요 {{name}}({{age}})!!</h2>
    {% endblock content %}
    ```
    
    ### 주의
    
    1.  변수명과 views.py의 매개변수의 이름이 같아야 한다.
    2. variable routing이 설정되면 반드시 매개변수로 받아야 한다
    3. variable routing이 적용된 주조는 반드시 값이 입력되어야 한다.