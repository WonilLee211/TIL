1. 프로젝트를 위한 폴더를 생성한다.
    1. `mkdir 폴더명`
2. bash 창을 열어서 프로젝트 폴더로 이동한다.
    1. `cd 폴더명`
3. 가상환경을 설정한다.
    1. `python -m venv venv`  : python -m venv 가상환경폴더명
4. 가상환경을 활성화 한다.
    1. `source venv/Script/activate` : v 탭 s 탭 a 탭 (Mac 인 경우 venv/Bin/activate)
    2. 활성화 된 상태

    
    c. `pip list` 를 통해서 가상환경이 정상적으로 적용되었는 확인
    
5. 장고를 설치한다. (필요한 패키지를 설치한다.)
    1. `pip install django==3.2`  : Django의 LTS 버전이 3.2 이기 때문 
    2. requirements에 작성된 패키지를 설치하는 방법 (가상환경을 새로 만들고 패키지를 설치해야 할 때)
        - `pip install -r requirements.txt` : retxtquirements 파일에 있는 패키지를 자동으로 설치
6. 패키지 리스트를 만들어준다.
    1. `pip freeze > requirements.txt` : 개발환경에서 사용하는 패키지의 버전을 명시하기 위함
7. 장고 프로젝트를 생성한다.
    1. `django-admin startproject config .`
        - django-admin startproject 프로젝트폴더명 [.]
            - 마지막에  `.` 이 있는 경우 현재 폴더에 바로 생성
            - `.` 이 없는 경우 프로젝트 폴더를 만들고 그 내부에 필요 폴더와 파일을 생성
8. 장고 application 생성한다.
    1. `python manage.py startapp articles`
        1. python manage.py startapp 앱이름
            - 앱이름은 복수형으로 짓는다.
    2. `settings.py` 에 방금 생성한 application을 등록한다.
        1. `INSTALLED_APPS` 리스트 내부에 어플리케이션 이름을 등록해 준다.
        2. 이 때 `,` 빠지지 않도록 주의해준다.

9. base.html 을 만들어 준다.
    1. base.html 은 코드의 재사용성을 높이기 위한 파일
    2. 위치는 전체 폴더 아래에 `templates` 라는 폴더를 생성한다.
    3. `templates` 폴더를 `settings.py` 에 등록한다.
        1. `TEMPLATES` 에 있는 `DIRS` 에 방금 생성한 폴더의 경로를 등록한다.
            
        2. `BASE_DIR / ‘templates’`
            
            - BASE_DIR : 전체 폴더 경로를 의미
    4. templates 폴더 내부에 `base.html` 파일을 생성한다.
        - cdn 주소 같이 포함
        - DTL의 block tag를 추가해야 한다.
            
            ```html
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            </head>
            <body>
                {% block content %}
                {% endblock content %}
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            </body>
            </html>
            ```
            
10. url 분리를 진행한다.
    1. 어플리케이션 폴더 내부에 `urls.py` 파일을 새롭게 생성한다.
    2. `urls.py` 내부에 코드를 작성한다.
        1. path 함수를 import 한다
        2. urlpatterns 라는 빈 리스트를 만들어 준다.
        3. app_name 을 설정해준다.
        - 최종 형태
        
        ```python
        from django.urls import path
        from . import views
        
        app_name = 'articles'
        urlpatterns = [
            
        ]
        ```
        
    3. 프로젝트 폴더에 있는 `urls.py` 에서 방금 생성한 `어플리케이션/urls.py` 를 등록해준다.
        1. include 함수를 import 한다.
        2. include 함수를 이용해서 urlpattern 에 등록한다.
