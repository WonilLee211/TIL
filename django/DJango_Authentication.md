
# the Django authentication system

- 인증과 권한 부여를 함께 제공(처리)함
- 이러한 기능을 어느 정도 결합시켜 인증시스템이라 함
- `django.contrib.auth`
- **Authentication(인증)**
    - 신원확인
    - 사용자가 자신이 누군지 확인하는 것
- Authorization(권한, 허가)
    - 권한부여
    - 인증된 사용자가 수행할 수 있는 작업을 결정
    

## -1. 사전설정

- 두번째 앱, `accounts` 생성 및 등록
- `$ python manage.py startapp accounts`
    - 인증관련 app name은 무조건 accounts(내부적으로 accounts를 사용하고 있기 때문)
    
    ```python
    # settings.py
    INSTALL_APPS = [
        'articles',
        'accounts',
        ...
    ]
    ```
    
- url 분리 및 맵핑
    
    ```python
    # crud/urls.py
    
    urlpattern = [
        ...,
        path('accounts/', include('accounts.urls'))
    ```
    
    ```python
    # accounts/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
    ]
    ```
    

## -2. Substituting a custom User Model

- 개발자들이 작성하는 일부 프로젝트가 django에서 제공하는 built-in user model의 기본 인증 요구 사항이 적절하지 않을 수 있음
    - 내 서비스에서 회원가입 시 username 대신 email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우 django user model
- 장고는 User model이 기본적으로 username을 식별값으로 사용하기 때문에 user model을 수정해야 함
    - `나중에 바꿀 일이 생기면 바꾸기 어려우니까 초기에 커스텀해놓고 시작하자`
    - `**AUTH_USER_MODEL**` 설정값의 **default user model을 재정의**할 수 있음

### **AUTH_USER_MODEL**

- 프로젝트에서 User를 나타낼 때 사용하는 모델
- 프로젝트가 진행되는 동안 변경 불가
- 프로젝트 시작 시 설정하기 위한 것
- 마이그레이션 전에 확정지어야 하는 값

## - 3. how to substitute a custom user model

- **대체하기**
    - AbstractUser를 상속받는 **커스텀 user 클래스 작성**
    - 기존 user 클래스도 AbstractUser를 상속받기 때문에 커스텀 user클래스도 완전히 같은 모습을 가지게 됨
        
        ```python
        # accounts/models.py
        
        from django.contrib.auth.models import AbstractUser
        
        class User(AbstractUser):
            pass # 일단 pass로 두고 선 대체를 선언해두고 시작해야 함
        ```
        
    - Django 프로젝트에 **user를나타내는데 사용하는 모델을** 방금 생성한 **커스텀 user모델로 지정**
        
        ```python
        # settings.py
        AUTH_USER_MODEL = 'accounts.User'
        ```
        
    - admin.py에 커스텀 user모델을 등록
        - 기본 user 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
        - **admin에서 관리하려고 할 때 작성**
        
        ```python
        #accounts/admin.py
        
        from django.contrib import admin
        **# admin page에서 user관리 page의 인터페이스를 설정
        from django.contrib.auth.admin import UserAdmin
        # 새롭게 정의한 user model
        from .models import User
        
        #어드민 사이트에 등록한다. 새롭게 정의한 User모델을 UserAdmin으로
        admin.site.register(User, UserAdmin)** 
        ```
        

### [참고] user 모델 상속 관계

- models.Model → class AbstractBaseUser → **class AbstractUser** → class User

### class AbstractUser

- 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 **추상 기본 클래스**
- **Abstract base classes(추상 기본 클래스)**
    - 몇 가지 **공통 정보를 여러 다른 모델을 넣을 때 사용하는 클래스**
    - 데이터 베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 **필드가 하위 클래스의 필드에 추가**됨
- **주의사항**
    - 중간 변경은 하지마 !(프로젝트 시작 때 설정하기)

### User model 대체 해야 하는 이유

- 새 프로젝트 시작할 때 기본 user 모델이 충분하더라도, 커스텀 user model 설정이 강력 권장
- 커스텀 user model은 기본 user model과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
- `단, **user 모델 대체 작업**은 프로젝트의 모든 **migrations 혹은 첫 migrate를 실행하기 전**에 작업 마치기`

### DB 초기화

- 프로젝트 중간일 경우
    1. migration 파일 삭제
        - migrations 폴더 및 __init__.py는 삭제하지 않음
        - 번호가 붙은 파일만 삭제
    2. db.sqlite3 삭제
    3. migrations 진행
        - makemigrations
        - migrate
        

여기까지 기본 세팅 

### custom User model 확인

- db에 appname_user의 하위속성 확인하기
- 기존엔 auth_user
- 커스텀 이후 accounts_user
- 명명 규칙 :   `appname_user`

---

# HTTP Cookies

## -1. HTTP

- Hyper Text Transfer Protocol
- HTML문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 시초
- 클라이언트-서버 프로토콜이라고도 함

## -2. 요청과 응답

### 요청(requests)

- 클라이언트(브라우저)에 의해 전송되는 메세지

### 응답(response)

- 서버에서 응답으로 전송되는 메세지

## -3. HTTP 특징

1. **비연결 지향(connectionless)**
    - 서버가 응답 후 연결 끊음
2. **무상태(stateless)**
    - 연결이 끊기는 순간 상태 정보가 유지되지 않음
    - 요청과 응답이 서로 완전히 독립적

### 로그인 상태 유지

- **쿠키와 세션**을 통해 서버와 클라이언트 간 지속적인 상태 유지

## -3. 쿠키(cookies)

- 상태가 있는 **세션**을 만들어주도록 함
- 서버가 사용자 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우, 서버를 통해 사용자의 컴퓨터에 설치되는 **작은 기록 정보 파일**
    1. 브라우저는 쿠키를 로컬 key-value 데이터 형태로 저장
    2. **동일한 서버 재요청 시 저장된 쿠키를 함께 전송(요청)**
- 두 요청이 동일한 브라우저에서 들어왔는지 아닌지 판달할 떄 사용
    - 로그인 상태 유지에 이용
    - stateless HTTP 프로토콜에서 상태 정보를 기억시켜주기 때문
- 웹페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고 클라이언트가 같은 서버에 재요청 시마다 요청과 함께 저장해둔 쿠키도 함께 전송

### **-3.1 쿠키 사용 목적**

1. **세션관리(sesstion management)**
    - **로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리**
2. 개인화(Personalization)
    - 사용자 선호, 테마 등의 설정
3. 트래킹(tracking)
    - 사용자 행동을 기록 및 분석
    

### - 3.2 쿠키를 이용한 장바구니 예시

- 장바구니에 상품 담기

### -3.3 세션(session)

- 사이트와 특정 브라우저 사이의 state를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
    - 재접속 시 쿠키를 서버에 전달
    - 서버는 session id를 확인해 알맞는 로직 처리
- session id는 세션을 구별하기 위해 필요
    - 쿠키에는 session id만 저장(안전성 보장)

### 3.4 쿠키 Lifetime(수명)

1. session cookie
    - 현재 세션(current session)이 종료되면 삭제됨
    - 브라우저 종료와 함께 세션이 삭제됨
2. persistent cookies
    - exipires 속성에 지정된 날짜 또는 max-age 속성에 지정된 기간이 지나면 삭제
    

### - 3.5 session in Django

- default : `database-backed sessions 저장방식`
    - sessions 정보는 **django DB**의 **django_session 테이블에 저장**
    - 설정을 통해 다른 저장방식으로 변경 가능
- Django는 특정 **session id를 포함하는 쿠키를 사용**해서 각각의 브라우저와 사이트가 연결된 session 알아냄
- Django는 우리가 session 메커니즘에 대부분을 생각하지 않게끔 도움

# Authentication in Web requests

- Django 인증관련 built-in forms 익히기
- https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.forms

## - 1. Login

- session을 Create하는 과정

### 1.1 AuthenticationForm

- **로그인을 위한 built-in form(일반 폼)**
    - 로그인하고자 하는 사용자 정보를 입력받음
    - 기본적으로 username과 password를 받아 데이터가 유효한지 검증
    - <mark>**일반 폼이어서 사용법 잘 숙지하기</mark>**
- request를 첫번째 인자로 취함

```python
# accouts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

```python
# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login 
# Create your views here.
def login(request):
    if request.method == 'POST':
        # form에 들어가야할 인자 : request, reqest.POST
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 유효성 검사 이 후
            auth_login(request, form.get_user()) # request를 첫번째 인자로 취함
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

### login()

- `login(request, user인스턴스, backend=None)`
- **사용자의 session 생성-DB에 저장/쿠키에 session-id 저장**
- **인증된 사용자**를 로그인시키는 로직으로 view함수에서 사용
- 현재 세션에 연결하려는 인증된 사용자가  있는 경우 사용
- Httprequest 객체와 User객체가 필요

### get_user()

- AuthenticationsForm 인스턴스 메서드
- **유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환**

### context processors

- `settings.py/templates`
- 템플릿이 렌더링될 때 호출 가능한 컨테스트 데이터 목록
- 작성된 컨텍스트데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨
- 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것
- `django.contrib.auth.context_processers.auth`

## Authentication with User

### django.contrib.auth.context_processers.auth

- 현재 로그인한 사용자를 나타내는 User클래스의 인스턴스가 탬플릿 변수 {{ user }}에 저장됨
    - 클라이언트가 로그인하지 않은 경우 AnonymousUser클래스의 인스턴스로 생성

## - 2. Logout

- session을 delete하는 과정

### 2.1 logout()

- `logout(request)`
- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않는 경우 오류를 발생시키지 않음
- 2가지 작업
    1. 현재 요청에 대한 session data를  DB에서 삭제
    2. 클라이언트 쿠키에서도 sessionid를 삭제
        - 이는 다른 사람이 동일한 웹 브라우저를 사용, 로그인하고 이전 사용자의 세션 데이터에 엑세스하는 것을 방지

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

```python

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="logout">
    </form>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

# Authentication with User

- User Object와 User CRUD에 대한 이해
    - 회원가입, 회원탈퇴, 회원정보수정, 비밀번호 변경
    

## -1. 회원가입

- Create
- `UserCreationForm` built-in form 사용

### 1.1 UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
- 3개의 필드를 가짐
    1. username(from the user model)
    2. Password1
    3. Password2
- 참고 : https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L75
- 회원가입 페이지 작성
    
    ```python
    # accounts/urls.py
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
        ...,
        path('signup/', views.signup, name='signup'),
    ]
    ```
    
    ```python
    # accounts/views.py
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
    
    def signup(request):
        if request.method=="POST":
            pass
        else:
            form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'accounts/signup.html', context)
    ```
    
    ```html
    <!-- accounts/signup.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>SIGNUP</h1>
      <form action="{% url 'accounts:signup' %} ">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    ```
    
- 회원가입 링크 작성 후 페이지 확인
    
    ```html
    <!-- base.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
    </head>
    <body>
      <div class="container">
        <h3>{{ user }}</h3>
        <a href="{% url 'accounts:login' %}">Login</a>
        <form action="{% url 'accounts:logout' %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="logout">
        </form>
        **<a href="{% url 'accounts:signup' %}">signup</a>**
        <hr>
        {% block content %}
        {% endblock content %}
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    </body>
    </html>
    ```
    
- 회원 가입 로직
    
    ```python
    # accounts/views.py
    
    def signup(request):
        if request.method=="POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'accounts/signup.html', context)
    ```
    

### 회원가입 진행 후 에러 페이지 확인

- `AttributeError at /accounts/signup/`
    - `manager isn't available:'auth.User' has been swapped for 'accounts.User'`
- 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문
- https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L106

### 1.2 Custom user & Built-in auth forms

- custom user와 기존 built-in forms 간의 관계
- custom user로 인한 built-in forms 변경

### AbstractBaseUser의 모든 subclass와 호환되는 forms

- 아래 Form 클래스는 User모델을 대체하더라도 커스텀하지 않아도 사용가능
    1. AuthenticationForm
    2. SetPassowordForm
    3. PasswordChangeForm
    4. AdminPasswordChangeForm
- 기존 User 모델을 참조하는 Form이 아니기 때문

### <mark>커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야하는 forms</mark>

1. **UserCreationForm**
2. **UserChangeForm**
- 두 form 모두 class Meta: model = User가 등록된 Form이기 때문에 반드시 커스텀(확장)해야 함
    
    ```python
    #accounts/form.py
    
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    
    # from .models import User
    # 장고에서 직접 참조하는 것을 싫어하기 때문에 간접 참조하기
    from django.contrib.auth.forms import get_user_model
    
    class CustomUserCreationForm(UserCreateForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
    
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
    ```
    
- **get_user_model()**
    - `현재 프로젝트에서 활성화된 사용자 모델(active user model)` 을 반환
    - 직접 참조하지 않는 이유
        - 예> 기존 User모델이 아닌 User 모델을 커스텀한 상황에서는 커스텀 User모델을 자동으로 반환해주기 때문
    - Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조
    
- CustomUserCreationForm()으로 대체하기
    
    ```python
    # accounts/views.py
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
    **from .forms import CustomUserCreationForm, CustomUserChangeForm**
    
    def signup(request):
        if request.method=="POST":
            **form = CustomUserCreationForm(request.POST)**
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            **form = CustomUserCreationForm()**
        context = {
            'form':form,
        }
        return render(request, 'accounts/signup.html', context)
    ```
    

### 회원가입 후 곧바로 로그인 진행

```python
# accounts/views.py
def signup(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            **# 공식문서에서 save()인스턴스함수가 반환하는지 확인하기**
            **user = form.save()
            # 회원가입 후 로그인
            auth_login(request, user)**
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

- https:/github.com/django/django/blob/main/django/contrib/auth/forms.py#L139
    - **# 공식문서에서 save()인스턴스함수가 반환하는지 확인하기**
    

## -2. 회원 탈퇴

- 회원 탈퇴하는 것은 DB에서 유저를 Delete하는 것과 같음
    
    ```python
    # accounts/urls.py
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
        ...,
        path('delete/', views.delete, name='delete'),
    ]
    ```
    
    ```python
    # accounts/views.py
    
    def delete(request):
        request.user.delete()
        return redirect('articles:index')
    ```
    
    ```python
    <!-- base.html -->
    
    <body>
      <div class="container">
        <h3>{{ user }}</h3>
        ...
        <hr>
        <form action=" {% url 'accounts:delete' %} " method="POST" >
          {% csrf_token %}
          <input type="submit" value="회원가입">
        </form>
        {% block content %}
        {% endblock content %}
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    </body>
    </html>
    ```
    

### [참고] 탈퇴하면서 해당 유저의 세션정보도 함께 지우고 싶을 경우

- 탈퇴(1) 후 로그아웃(2) 순서가 바뀌면 안됨
- 먼저 로그아웃해버리면 해당 요청 객체 정보가 없어지기 때문
    
    ```python
    # accounts/views.py
    
    def delete(request):
        # 회원 탈퇴는 DB를 수정하느 것이기에 POST일 때만 동작
        if request.method=='POST':
            # user 정보는 request 내부에 가지고있어서
            # 따로  db에서 불러올 필요없음
            request.user.delete()
            auth_logout(request)
            return redirect('articles:index')
    ```
    

## -3. 회원정보 수정

- `UserChangeForm` built-in form 사용

### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
- ModelForm이기 때무에 instance인자로 기존 user 데이터 정보를 받는 구조 또한 동일!
- CustomUserChangeForm으로 확장
    
    ```python
    # accounts/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
        ...,
        path('update/', views.update, name='update'),
    ]
    ```
    
    ```python
    # accounts/views.py
    
    def update(request):
        if request.method=="POST":
            pass
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form':form
        }
        return render(request, 'accounts/update.html', context)
    ```
    
    ```html
    <!-- accounts/update.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>회원정보수정</h1>
      <form action="{% url 'accounts:update' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    ```
    
    ```html
    <!-- base.html -->
    
    <body>
      <div class="container">
        <h3>{{ user }}</h3>
        ...
    
        <a href=" {% url 'accounts:update' %} ">회원정보수정</a>
        {% block content %}
        {% endblock content %}
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    </body>
    </html>
    ```
    
- **UserchangeForm 사용 시 문제점**
    - 일반 사용자가 접근해서는 안될 fields까지 모두 수정하게 됨
        - admin 인터페이스에서 사용되는 ModelForm이기 때문
    - **해결책**
        - 회원 정보 수정할 수 있는 field 제한하기
        - 서브클래스 CustomUserChangeForm에서 접근 가능한 필드 조정
        
        ```python
        from django.contrib.auth.forms import UserCreationForm, UserChangeForm
        from django.contrib.auth.forms import get_user_model
        
        class CustomUserChangeForm(UserChangeForm):
            class Meta(UserChangeForm.Meta):
                model = get_user_model()
                fields = ('email','first_name', 'last_name',)
        ```
        
        - **User model 상속 구조 살펴보기**
            1. UserChangeForm 클래스 구조 확인
                - Meta클래스를 보면 User model을 참조하는 ModelForm이라는 것을 확인
                - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147
            2. User 클래스 구조 확인
                - 실제로 User클래스는 Meta클래스를 제외한 코드가 없고 AbstractUser클래스를 상속받고 있음
            - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405
            1. AbstractUser 클래스 구조 확인
                - 클래스 변수명들을 확인해보면 회원수정 페이지에서 봤던 필드들과 일치한다는 것을 확인할 수 있음
                - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L334
            2. 공식 문서의 User모델 Fields 확인
                - https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model
- 회원정보 수정 로직 작성
    
    ```python
    def update(request):
        if request.method == 'POST':
            **form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')**
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
    ```
    

## -4. 비밀번호 변경

### 4.1 PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Forms
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

### 4.2 비밀번호 변경 페이지 작성

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # password라는 키워드가 겹칠 수 있기 때문에 다른 이름으로 명명
    path('password/', views.change_passwored, name='change_password'),
]
```

```python
def change_password(request):
    if request.method=='POST':
        **form = PasswordChangeForm(request.user, request.POST)**
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 인자가 기존과 다름 주의
        **form = PasswordChangeForm(request.user)**
    context = {
        'form':form
    }
    return render(request, 'account/change_password.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Change Password</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

### 문제 : 암호 변경 시 세션 무효화

- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보 불일치
- 로그인 상태 유지 못함
- **해결책**
    - 세션 무효화 방지하기

### update_session_auth_hash()

- `update_session_auth_hash(request, user)`
- 현재 요청(current request)과 새 session data가 파생될 업데이트된 사용자 객체를 가져오고, session data에 업데이트해주기
- 암호가 변경되어도 로그아웃되지 않도록 새로운 password의 session data로 session을 업데이트

```python
# accounts/views.py
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 일반 폼을 상속받았지만, save()함수가 정의되어 있음
            user = form.save()
            # 비밀번호가 변경되면 session의 유저데이터와 일치하지 않게 되는 현상 발생
            # session의 유저정보를 업데이트 시켜야 한다.
            # 인자 : request, 유저정보
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        # 로그인한 유저의 비밀번호를 저장해야 하기 때문에 
        # 첫번째 인자로 user 정보를 넣어야 한다.
        # 일반폼이라서 인스턴스형태로 넣지않고 바로 request.user를 인자로 넣는다.
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,

    }
    return render(request, 'accounts/password.html', context)
```

# Limiting access to logged-in users

- 로그인 사용자에 대한 접금 제한하기
- 로그인 사용자에 대해 접근을 제한하는 2가지 방법
    1. the raw way
        - `is_authenticated` attribute
    2. the `login_required` decorators

## - 1. is_authenticated

- User model의 속성 중 하나
- 사용자가 로그인 상태인지 비로그인 상태인지만 확인
    - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
    - AnonymousUser에 대해 항상 False
- `@property` 데코레이터가 붙어있어서 그냥 호출해서 사용할 수 있음
- 사용법
    - `request.user.is_authenticated`
- 주의 : 권한과는 관련없으며, 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인안함
    
    ```python
    class AbstractBaseUser(models.Model):
        ...,
        @property
        def is_authenticated(self):
        """
        always return True if the user has been authenticated in templates.
        """
        return True
    ```
    
- https://github.com/django/django/blob/main/django/contrib/auth/base_user.py#L56

- **적용**
    - 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정
    
    ```python
    <!-- base.html -->
    
        **{% if request.user.is_authenticated %}**
          <h3>{{ user }}</h3>
          <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout">
          </form>
          <form action="{% url 'accounts:delete' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="회원탈퇴">
          </form>
          <a href="{% url 'accounts:update' %}">회원정보수정</a>
        **{% else %}**
          <a href="{% url 'accounts:login' %}">Login</a>
          <a href="{% url 'accounts:signup' %}">Signup</a>
        **{% endif %}**
    ```
    
    - 여전히  url을 알고 있다면 비로그인 상태로 접근할 수 있음
- **적용2**
    - 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리하기
    
    ```python
    <!-- articles/index.html -->
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Articles</h1>
      **{% if request.user.is_authenticated %}
        <a href="{% url 'articles:create' %}">CREATE</a>
      {% else %}
        <a href=" {% url 'accounts:login' %} ">새 글을 작성하려면 로그인하세요</a>
      {% endif %}**
      <hr>
      {% for article in articles %}
        <p>글 번호 : {{ article.pk }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
        <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
        <hr>
      {% endfor %}
    {% endblock content %}
    ```
    
    - 여전히 비로그인 상태로 url 직접 입력으로 접근 가능
- 적용3
    
    ```python
    # accounts/views.py
    
    def login(request):
        if request.user.is_authenticated:
            return redirect('articles:index')
    ```
    

### login_required

- `login_required` decorator
- 로그인 상태에서 정상적으로 view함수 실행
- 비로그인 상태에서 setting.py의 LOGIN_URL 문자열 주소로 redirect
    - [참고] : LOGIN_URL의 기본 값은 /accounts/login/
    - 두번째 app 이름을  accounts로 했던 이유 중 하나
    
    ```python
    from django.contrib.auth.decorators import login_required
    
    **@login_required**
    @require_POST
    def delete(request):
        pass
    
    **@login_required**
    @require_http_methods(['GET', 'POST'])
    def update(request):
        pass
    
    **@login_required**
    @require_http_methods(['GET', 'POST'])
    def change_password(request):
        pass
    ```
    

### login_required 적용 확인하기

- /articles/create/로 강제 접속 시도해보기
- 로그인 페이지로 리다이렉트 후 `/accounts/login/?next=/articles/create/` url 확인하기
- 인증 성공 시 사용자가 redirect 되어야하는 경로는 “next”라는 쿼리 문자열 매개변수에 저장됨
    - 예시 > /accounts/login/?next=/articles/create

### “next” query string parameter

- 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect하기 위해 Django가 제공해주는 쿼리 스트링 파라미터
- 해당 값을 처리할지 말지는 자유이며 별도로 처리해주지 않으면  view에 설정한 redirect경로로 이동하게 됨
    
    ```python
    def login(request):
        if request.user.is_authenticated:
            return redirect('articles:index')
    
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            # form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                # 로그인
                auth_login(request, form.get_user())
                **return redirect(request.GET.get('next') or 'articles:index')**
    ...
    ```
    
- url요청이니깐 GET으로 받아오기 > 오류라면 index로 보내기
- **주의사항**
    - 만약 login 탬플릿에서 form action이 작성되어 있다면 동작하지 않음
    - 해당 action 주소 next파라미터가 적성되어있는 현재 url이 아닌 /accounts/login/으로 요청을 보내기 때문
    - {% url ‘accounts:login’ %} 지우기
    
    ```html
    <!-- accounts/login.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>LOGIN</h1>
    
      <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    ```
    

### @login_required vs @require_POST 로 발생하는 구조적 문제

1. 먼저 비로그인 상태로 detail페이지에서 게시글 삭제 시도
2. delete view함수의 @login_required로 인해 로그인 페이지로 리다이렉트
    - https://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/
3. redirect로 이동한 로그인 페이지에서 로그인 진행
4. delete view함수의 @require_POST로 인해 405 상태 코드를 받게 됨
    1. 405(Method Not Allowed) status code
    2. 로그인 성공 이후 GET method로 next 파라미터 주소에 리다이렉트되기 때문
        - `GET / articles/1/delete/ HTTP/1.1" 405 0`
        
- **2가지 문제**
    1. redirect 과정에서 POST요청 데이터의 손실
    2. redirect로 인한 요청은  GET 요청 메서드로만 요청됨
- **해결방안**
    - **@login_required는  GET request method를 처리할 수 있는 View함수에서만 사용해야 함**
    - POST method만 허용하는 delete같은 함수는 내부에서는 is_authenticated 속성값을 사용해서 처리
        
        ```python
        # articles/views.py
        
        @require_POST
        def delete(request):
            **if request.user.is_authenticated:**
                request.user.delete()
                auth_logout(request)
            return redirect('articles:index')
        ```
        

# summary

- the Django authentication system
    - user 모델 대체하기
- HTTP cookies
    - 상태가 있는 세션 구성
- Authentication in Web requests
    - Auth built-in form 사용하기
- Authentication with User
    - User Object와 User CRUD