# STATIC

# Managing static files

- 개발자가 **서버에 미리 준비한** 혹은 **사용자가 업로드한 정적 파일**을 클라이언트에게 제공한 방법

## 1. 정적파일

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
    - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- `파일 자체가 고정`되어있고 서비스 중에서 추가되거나 `변경되지않고 고정`되어 있음
    - 예시 : 웹 사이트는 일반적으로 이미지, JS 또는 CSS와 같은 미리 준비된 추가 파일을 제공해야 함
- Django에서는 이러한 파일들을 “static file”이라 함
    - `staticfiles` 앱을 통해 정적 파일과 관련된 기능을 제공

## 2. Media file

- 미디어 파일
- 사용자가 웹에서 업로드 하는 정적 파일(user_uploaded)

## 3. 웹 서버와 정적 파일

- 특정 위치(url)에 있는 자원을 `요청(http request)`받아서
- `응답(http responce)`를 처리하고 제공(serving)하는 것
- 자원과 자원에 접근 가능한 주소가 있다는 의미
    - `사진 파일을 얻기 위한 경로인 웹 주소(URL)가 존재`함
- 웹서버는 요청받은 url로 서버에 존재하는 정적자원을 제공해야 함

## 4. Django에서 정적파일을 구성하고 사용하기 위한 몇가지 단계

1. INSTALLED_APP에 'django.contrib.staticfiles'가 존재하는지 확인하기
2. settings.py에서 STATIC_URL을 정의하기
3. 앱의 static 폴더에 정적 파일 위치하기
    - `my_app/static/sample_img.jpg`
4. 탬플릿에서 static 탬플릿 태그를 사용하여 지정된 경로에 있는 `정적 파일의 url 만들기`
    
    ```python
    {% load static %}
    <img src="{% static 'sample_img.jpg' %}" alt="sample image">
    ```

## 5. Django template tag

- `{% laod %}` : 특정 라이브러리, 패키지에 등록된 `모든 탬플릿 태그와 필터를 로드`(built-in되지 않은 태그 쓸 때)
- `{% static '' %}`  : STATIC_ROOT에 저장된 정적 파일에 연결

## 6. static files 관련 Core Settings

1. **STATIC_ROOT**
    - Default : None
    -  설정 : `STATIC_ROOT = BASE_DIR / 'staticfiles'`
    - `$python manage.py collectstatic` 실행 시, staticfiles를 볼 수 있음
    - Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 놓은 경로
    - `collectstatic`이 `배포`를 위해 정적파일을 한 곳에 모아둔 디렉토리의 `절대 경로`
    - `**개발과정에서 settings.py의 DEBUG값이 True라면 해당값은 반영되지 않음**`
    - 실 서비스 환경(배포 환경)에서 Django의 모든  정적 파일을 다른 웹서버가 직접 제공하기 위해 사용
    - 배포 환경에서는 Django를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 `다른 서버는 장고에 내장되어있는 정적파일을 사용`

2. **STATICFILES_DIRS**
    - Defalut : [] (빈 리스트)
    - `apps/static/` 디렉토리 경로를 사용하는 것 외에 `추가적인 정적파일 경로 목록을 정의하는 리스트`

3. **STATIC_URL(중요)**
    - Default : None
    - STATIC_ROOT에 있는 정적파일을 참조할 떄 사용할 URL
    - 개발단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로(기본경로) 및 /STATICFILES_DIRS에 정의된 추가 경로들을 탐색
    - `실제 파일이나 디렉토리가 아니며 URL로만 존재`
    - 비어있지 않는값으로 설정한다면, 반드시 slash(/)로 끝나야 함


### [참고] 소프트웨어 배포(deploy)

- 프로그램 및 애플리케이션을 서버와 같은 기기에 설치하여 서비스를 제공하는 것
- 클라우드 컴퓨팅 서비스(AWS)에 프로그램 및 어플리케이션을 설치해 제공하는 것

### [참고] collectstatic

- STATIC_ROOT에 Django프로젝트의 모든 정적 파일 설치
    
    ```python
    # settings.py
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```
    
    ```python
    $ python manage.py collectstatic
    
    # 133 static files copied to 'C:\Users\lwi99\ssafy8th\webex_student\django\django\07_django\staticfiles'.
    ```
    
    - 어드민 페이지를 구성하는 CSS, JS 등 있음을 볼 수 있음
    - 결과를 보고 지우기


- STATIC_ROOT에 Django프로젝트의 모든 정적 파일 설치
    
    ```python
    # settings.py
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```
    
    ```python
    $ python manage.py collectstatic
    
    # 133 static files copied to 'C:\Users\lwi99\ssafy8th\webex_student\django\django\07_django\staticfiles'.
    ```
    
    - 어드민 페이지를 구성하는 CSS, JS 등 있음을 볼 수 있음
    - 결과를 보고 지우기
    

## 7. STATIC FILES 사용하기

### 7.1 가져오기

- static file 가져오는 2가지 방법
    1. 기본 경로(/my_app/static/...)에 있는 static file 가져오기
        
        ```python
        # settings.py
        STATIC_URL = '/static/'
        ```
        1. `my_app/static/my_app/ 폴더만들어서 이미지 넣기`
        
    2. 추가 경로에 있는 static file 가져오기
        
        ```python
        # settings.py
        STATICFILES_DIRS = [
            BASE_DIR / 'static',
        ]
        ```
        1. project에 static/ 폴더 만들고 이미지 넣기

- 결과 확인

    ```django
    # index.html

    {% extends 'base.html' %}
    {% load static %}

    {% block content %}
        # 기본경로 정적 파일
        <img src="{% static 'articles/cutepuppy.jfif' %} " alt="sample">
        # 127.0.0.1:8000/static/articles/cutepuppy.jfif 로 요청됨

        # 추가 경로 정적 파일
        <img src="{% static 'google1.png' %} " alt="sample2">
        # 127.0.0.1:8000/static/cutepuppy.jfif 로 요청됨

    ```

### 7.3 STATIC_URL 확인하기

- Django가 해당 이미지를 클라이언트에게 응답하기 위해 Image url 확인하기
    - 개발자 도구 - inspect 버튼을 통해 확인
- **‘static_url + static file 경로’로 설정됨**
    - http://127.0.0.1:8000/static/articles/sample_img_1.png

- 개발자도구 - network에서 request url확인해보기
    - 클라이언트에게 이미지를 응답하기 위한 요청 url을 만든 것