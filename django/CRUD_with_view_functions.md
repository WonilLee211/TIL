# CRUD with view functions

### - 사전준비

- **base 템플릿 작성**
    1. bootstrap CDN 및 템플릿 추가 
        
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">   
            <title>
                **{% block title %}
                {% endblock title %}**
            </title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        </head>
        <body>
            **{% block content %}
            
            {% endblock content %}**
        
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
        </body>
        </html>
        ```
        
        ```python
        TEMPLATES = [
            {
                ...,
                'DIRS': [BASE_DIR / 'templates'],
                'APP_DIRS': True, # 장고에서 자동으로 app 안에 templates 안에 파일을 탐색하는 옵션
                ...,
            }
        ]
        ```
        
- **url 분리 및 연결**
    
    ```python
    # articles/urls.py
    from django.urls import path
    from . import views
    app_name = 'articles'
    urlpattern = [
        path('', views.index, name='index'),
    ]
    ```
    
    ```python
    # config/urls.py
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ]
    ```
    

## - 1. READ 1(index page)

### 모델 생성

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    # CharField : 글자제한으로 문자를 저장하기 위한 필드
    # TextField : 글자 제한 없이 문자를 저장하기 위한 필드
    title = models.CharField(max_length=225)
    content = models.TextField()

    def __str__(self):
        return self.title
```

### 전체 게시글 조회

```python

# articles/views.py
from django.shortcuts import render, redirect
from .models import Post

# 모든 게시글의 목록을 보여주는 부분
def index(request):
    # 모든 게시글의 데이터가 필요
    # 1. 모든 데이터를 확보
    posts = Post.objects.all()
    # 2. 확보한 데이터를 template에 게시(, 즉 전달해야 한다.)
    context = {
        'posts':posts
    }

    return render(request, 'articles/index.html', context)
```

```html
<!-- templates/articles/index.html -->
{% extends 'base.html' %}
{% block content %}
<h1> Article </h1>
<hr>
  {% for article in articles %}
    <p> 글 번호 : {{article.pk}}</p>
    <p> 글 제목 : {{article.title}}</p>
    <p> 글 내용 : {{article.content}}</p>
  {% endfor %}
{% endblock content %}
```

## -2. CREATE

- CREATE 로직을 구현하기 위해서는 필요한 view 함수
    1. 사용자가 입력 받을 페이지를 렌더링하는 함수 1개
        - “new” view fuction
    2. 사용자가 입력한 데이터를 전송받아 DB에 저장하는 함수 1개
        - “create” view function
    

### New

```bash
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpattern = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]
```

```python
# articles/views.py
from django.shortcuts import render

# 글 작성을 위한 new, create
def new(request):
    return render(request, 'articles/new.html')
```

```html
<!-- templates/articles/new.html -->

{% extends 'base.html' %}
{% block content %}
<h1>NEW</h1>
<form action="#" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">content: </label>
    <textarea name="content" ></textarea>
    <input type="submit">
</form>
<hr>
<a href=" {% url 'articles:index' %} ">[back]</a>
{% endblock content %}
```

- new 페이지로 이동할 수 있는 하이퍼링크 작성

```html
<!-- templates/articles/index.html -->

{% extends 'base.html' %}
{% block content %}
<h1>Articles</h1>
<a href=" {% url 'articles:new' %} ">NEW</a>
{% endblock content %}
```

### create

```python
# article/urls.py

urlpattern = [
    ....
    path('create/', view.create, name='create'),
]
```

```python
# articles/views.py

# 사용자가 작성한 데이터를 받아서 db에 저장하는 역할
def create(request):
    # 데이터를 저장하기 위해서는 사용자의 데이터를 확보해야 한다.
    # print(request.GET)
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 확보한 데이이터를 db에 저장 > db 구축
    
    # 데이터를 db에 저장하는 방법은 3가지
    # 1st : models.py에 Post클래스 인스턴스 생성 - 다른 파일은 무조건 import 하기
    post = Post()
    post.title = title
    post.content = content
    post.save()

    # 2nd : Post 클래스의 인스턴스 생성(클래스 변수를 같이 줘)
    # post = Post(title=title, content=content)
    # post.save()

    # 3rd : QuerySet API - create 메서드 사용
    # 반환되는 인스턴스는 이미 db에 저장된 데이터
    # post = Post.objects.create(title=title, content=content)

****    return render(request, 'articles/create.html')
```

- **2번 생성방식을 사용하는 이유**
    - create메서드가 더 간단해 보이지만 추후 데이터가 저장되기 전에 **유효성 검사 과정**을 거치게 될 예정
    - 유효성 검사가 진행된 후에 save메서드가 호출되는 구조를 택하기 위함
- 게시글 작성 후 확인

```html
<!-- templates/articles/create.html -->

{% extends 'base.html' %}
{% block content %}
  <h1>성공적으로 글이 작성되었습니다.</h1>
{% endblock content %}
```

```html
<!-- templates/articles/new.html -->
{% extends 'base.html' %}
{% block content %}
<h1>NEW</h1>
<form action=**"{% url 'articles:creat' %}"** method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">content: </label>
    <textarea name="content" cols="30" rows="5"></textarea>
    <input type="submit">
</form>
<hr>
<a href=" {% url 'articles:index' %} ">[back]</a>
{% endblock content %}
```

- c게시글 작성 후 index 페이지로 돌아가도록 함

```python
#article.views.py
def create(request):
    ....
    return render(request, 'articles/index.html')
```

### 2가지 문제 발생

1. index 페이지가 출력되지만 게시글 조회가 되지 않음
    - create함수에서 index.html문서를 렌더링할 때 context 데이터와 함께 렌더링하지 않았기 때문
    - index 페이지 url로 다시 요청을 보내면 정상적으로 출력됨
2. 게시글 작성 후 URL은 여전히 create에 머물러 있음
    - index view 함수를 통해 렌더링 된 것이 아니기 때문
    - index view 함수의 반환 값이 아닌 단순히 index 페이지만  render되었기 때문

### rediect() - Django shortcut function

- 인자에 작성된 곳으로 요청을 보냄
- 사용가능한 인자
    1. view name(url pattern name) `return redirect('articles:index')` 
    2. absolute or relative url `return redirect('/articles/')`

```python

from django.shortcuts import render, **redirect**

# 사용자가 작성한 데이터를 받아서 db에 저장하는 역할
def create(request):
    # 데이터를 저장하기 위해서는 사용자의 데이터를 확보해야 한다.
    # print(request.GET)
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 확보한 데이이터를 db에 저장 > db 구축
    
    # 데이터를 db에 저장하는 방법은 3가지
    # 1st : models.py에 Post클래스 인스턴스 생성 - 다른 파일은 무조건 import 하기
    post = Post()
    post.title = title
    post.content = content
    post.save()

    # 2nd : Post 클래스의 인스턴스 생성(클래스 변수를 같이 줘)
    # post = Post(title=title, content=content)
    # post.save()

    # 3rd : QuerySet API - create 메서드 사용
    # 반환되는 인스턴스는 이미 db에 저장된 데이터
    # post = Post.objects.create(title=title, content=content)

    **# 글 작성하면 다음 뜨는 페이지
    # 선택 1. index 페이지로 이동해서 전체 데이터 목록을 보자
    # return redirect('articles:index')
    # 선택 2. 방금 작성한 글 페이지로 이동
    return redirect('articles:detail', posk.pk)**
```

- **동작원리**
    1. 클라이언트가 create url로 요청
    2. create view함수의 redirect함수가 **302 status code**를 응답
    3. 응답 받은 브라우저는 redirect인자에 담긴 주소(index)로 사용자를 이동시키기 위해 index url로 Django에 재요청
    4. index page를 정상적으로 응답받음(200 status code)

### [참고] 302 Found

- HTTP reosponse status code 중 하나
- 해당 상태 코드를 응답 받으면 **브라우저는 사용자를 해당 URL의 페이지를 이동시킴**

### HTTP response status code

- 클라이언트에게 특정 HTTP**요청이 성공적으로 완료되었는지 여부**를 알려줌
- 응답의 5 그룹
    1. Informational responses (1xx)
    2. Successful reponses (2xx)
    3. Redirection Messages (3xx)
    4. Client error responses (4xx)
    5. Server error responses (5xx)

---

### HTTP request method

- **GET**
    - **특정 리소스 조회 요청**할 때 사용
    - 반드시 데이터 가져올 때만 사용해야 함
    - DB에 변화를 주지 않음
    - CRUD에서 **R 역할**
    - HTML의 a tag : 특정 페이지 조회하는 요청을 보내는 태그
        - GET 방식 사용
- **POST**
    - 서버로 데이터를 전송할 때 사용
    - 서버에 변경사항을 만듦
    - 리소스 생성 및 변경을 위해 **HTTP body에 담아 전송**
        - GET의 쿼리 스트링 파라미터와(url에 담음)의 차이점
    - CRUD에서 C/U/D 역할을 담당

### - POST method 적용

```html
<!-- templates/articles/new.html -->

{% extends 'base.html' %}

{% block content %}
<h1>글 작성하기</h1>
<form action="{% url 'articles:create' %}" **method="POST"**>
    <label for="title" >글 제목</label>
    <input type="text" id="title" name="title"><br>
    <label for="content" id="content" name="content">글 내용</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
    <button>글쓰기</button>
</form>

{% endblock content %}
```

- CSRF missing  error
    - CSRF 토큰 : 해킹 방지 보안 토큰
    - `{% csrf_token %}` 를 form태그 내부에 작성

```python
def create(request):
    title = request.**POST**.get('title')
    content = request.**POST**.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()
 
    return redirect('articles:index')
```

### [참고] 403 Forbidden

- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
- 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨
- “게시글을 작성할 권한이 없다” = Django 입장에서 “작성자가 누구인지 모르기 떼문에 함부로 작성할 수없다”
- 모델을 조작할 때 최소한의 신원 확인이 필요하기 때문

### [참고] CSRF

- Cross-Site-Request-Forgery
- “사이트 간 요청 위조”
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

### [참고] CSRF 공격 방어

- “Security Token 사용 방식(CSRF Token)”
    1. 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 **요청마다 해당 난수 값을 포함시켜 전송**시키도록 함
    2. 서버에서 요청받을 때마다 전달된 token값이 유효한지 검증
    3. 일반적으로 데이터 변경이 가능한  POST, PATCH, DELETE Method등에 적용
    4. Django-DTL : `{% csrf token %}`
        - 없다면 Django  서버의 응답은 `403 forbidden`
- **주의 : 외부 URL로 향하는 POST form에 대해서  CSRF token 사용 금지**

## -3. READ2(detail page)

- 개별 게시글 상세 페이지 제작
- 문제 : 모든 게시글마다 뷰 함수와 템플릿 파일을 만들 수 없음
    - varible routing으로 글의 번호(pk)활용- 하나의 뷰 함수와 탬플릿 파일로 대응
    
    ```python
    # articles/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        # 글 조회를 위한 detail
        path('detail/<post_id>/', views.detail, name='detail'),
     ]
    ```
    
    ```python
    # articles/views.py
    from django.shortcuts import render, redirect
    from .models import Post
    
    # 글 내용 조회 ( 하나의 글 데이터 필요)
    def detail(request, post_id):
        # Post.objects.get(컬럼명=찾는값)
        # 사용자가 무슨 글을 클릭했지?
        # 사용자가 클릭한 글 정보를 전달 받아야 하는데
            # 주소로 글의 정보를 전달받자(variable routing)
            # 글을 클릭할 때 전달해야 함.(index페이지에서 글을 클릭)
            # query api에서 get 메서드는 유일한 값을 이용해서 데이터를 찾음
            # index.html 글클릭 > id 주소 전달 > 넘겨준 주소를 변수로 사용
            # > urls.py에서 변수 설정(<post_id>) > views.py에서 넘어오는 변수를 인자로 받기(이름은 동일하게!)
        post = Post.objects.get(id=post_id) # 전달받은 아이디로 데이터 가져오기
        context = {
            'post':post,
        }
        return render(request, 'articles/detail.html', context)
    
    # 모든 게시글의 목록을 보여주는 부분
    def index(request):
        # 모든 게시글의 데이터가 필요
        # 1. 모든 데이터를 확보
        posts = Post.objects.all()
        # 2. 확보한 데이터를 template에 게시(, 즉 전달해야 한다.)
        context = {
            'posts':posts
        }
    
        return render(request, 'articles/index.html', context)
    ```
    
    ```html
    <!-- templates/articles/detail.html -->
    
    {% extends 'base.html' %}
    {% block content %}
    <h1>{{post.id}}번 글</h1>
    <p>제목 : {{post.title}}</p>
    <p>내용 : {{ post.content }}</p>
    
    <hr>
    {% comment %} pk = id {% endcomment %}
    <a href="{% url 'articles:edit' post.id %}">수정하기</a>
    <a href="{% url 'articles:index' %}">글 목록 보기</a>
    <hr>
    
    {% endblock content %}
    ```
    
    ```html
    <!-- templates/articles/index.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
    <h2>index</h2>
    
    <a href=" {% url 'articles:new' %} ">글작성하기</a>
    <hr>
    {% for post in posts %}
    <p>
      {% comment %} 
      variable routing으로 전달하는 값은 유일한 값이어야 함 
      id 값 사용하기
      {% url 'app_name:path_name' 주소로 전달할 값 %}
      {% endcomment %}
    
      **<a href="{% url 'articles:detail' post.pk %}">{{post.title}}</a>**
      
    </p>
    {% endfor %}
    
    {% endblock content %}
    ```
    
- redirect 인자변경
    
    ```python
    # v사용자가 작성한 데이터를 받아서 db에 저장하는 역할
    def create(request):
        # 데이터를 저장하기 위해서는 사용자의 데이터를 확보해야 한다.
        # print(request.GET)
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 확보한 데이이터를 db에 저장 > db 구축
        
        # 데이터를 db에 저장하는 방법은 3가지
        # 1st : models.py에 Post클래스 인스턴스 생성 - 다른 파일은 무조건 import 하기
        post = Post()
        post.title = title
        post.content = content
        post.save()
    
        # 2nd : Post 클래스의 인스턴스 생성(클래스 변수를 같이 줘)
        # post = Post(title=title, content=content)
        # post.save()
    
        # 3rd : QuerySet API - create 메서드 사용
        # 반환되는 인스턴스는 이미 db에 저장된 데이터
        # post = Post.objects.create(title=title, content=content)
    
        # 글 작성하면 다음 뜨는 페이지
        # 선택 1. index 페이지로 이동해서 전체 데이터 목록을 보자
        # return redirect('articles:index')
        # 선택 2. 방금 작성한 글 페이지로 이동
        return **redirect('articles:detail', posk.pk)**
    ```
    

## - 4. DELETE

- **urls**
    - 삭제하고자 하는 특정글을 조회 후 삭제 >> variable routing으로 데이터 받아서 삭제
    
    ```python
    # articles/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        path('delete/<post_id>/', views.delete, name='delete'),
    ]
    ```
    
- views.py
    
    ```python
    # articles/views.py
    
    from django.shortcuts import render, redirect
    from .models import Post
        
    def delete(request, post_id):
        # POST 요청일 때만 삭제하게 만들어줘야 한다.
        if request.method == "POST":
            # 1. 삭제할 글 찾아오기
            post = Post.objects.get(pk=post_id)
            # 2. 삭제하기
            post.delete()
    
        return redirect('articles:index')
    ```
    
- templates/details.html
    
    ```html
    <!-- templates/articles/details.html -->
    
    {% extends 'base.html' %}
    {% block content %}
    <h1>{{post.id}}번 글</h1>
    <p>제목 : {{post.title}}</p>
    <p>내용 : {{ post.content }}</p>
    
    <hr>
    {% comment %} pk == id {% endcomment %}
    <a href="{% url 'articles:edit' post.id %}">수정하기</a>
    <a href="{% url 'articles:index' %}">글 목록 보기</a>
    <hr>
    
    {% comment %} <a href=" {% url 'articles:delete' post_id %} ">글 삭제</a> {% endcomment %}
    **<form action=" {% url 'articles:delete' post.pk %}" method="POST">
        {% csrf_token %}
        <button>삭제하기</button>
    </form>**
    {% endblock content %}
    ```
    

## - 5. UPDATE

- 수정은 2 개의 view함수 요구됨
    1. 사용자의 입력을 받을 페이지를 렌더링할 함수 1개
        - “edit” view function
    2. 사용자가 입력한 데이터를 전송받아  BD에 저장하는 함수 1개
        - “update” view function
1. 사용자의 입력을 받을 페이지 함수
    - **urls**
        
        
        ```python
        # articles/urls.py
        
        from django.urls import path
        from . import views
        
        app_name = 'articles'
        urlpatterns = [
            path('edit/<post_id>/', views.edit, name='edit'),
         
        ]
        ```
        
    - views.py
        
        ```python
        # articles/views.py
        
        from django.shortcuts import render, redirect
        from .models import Post
            
        def edit(request, post_id):
            # 어떤 글을 수정하고 있는지 post_id로 확인 가능
            post = Post.objects.get(pk=post_id)
            context = {
                'post':post,
            }
            return render(request, 'articles/edit.html', context)
        ```
        
    - templates/edit.html
        
        ```html
        <!-- templates/articles/edit.html -->
        
        {% extends 'base.html' %}
        {% block content %}
        <h1>글 수정하기</h1>
        {% comment %} 목적지는 우리가 만들면 된다! {% endcomment %}
        <form action="{% url 'articles:update' post.pk %}" method="POST">
            {% csrf_token %}
            <label for="title" >글 제목</label>
            **{% comment %} 기존의 값을 보여줘야 한다. {% endcomment %}**
            <input type="text" id="title" name="title" **value="{{post.title}}**"><br>
            <label for="content" id="content" name="content">글 내용</label>
            **{% comment %} textarea 태그는 value속성이 없으므로 태그 내부 값으로 작성 {% endcomment %}**
            <textarea name="content" id="content" cols="30" rows="10" >**{{post.content}}**</textarea><br>
            <button>글쓰기</button>
        </form>
        
        {% endblock content %}
        ```
        
2. edit페이지로 이동할 하이퍼링크 생성
    
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1>{{post.id}}번 글</h1>
    <p>제목 : {{post.title}}</p>
    <p>내용 : {{ post.content }}</p>
    
    <hr>
    {% comment %} pk = id {% endcomment %}
    **<a href="{% url 'articles:edit' post.id %}">수정하기</a>**
    <a href="{% url 'articles:index' %}">글 목록 보기</a>
    <hr>
    
    {% comment %} <a href=" {% url 'articles:delete' post_id %} ">글 삭제</a> {% endcomment %}
    <form action=" {% url 'articles:delete' post.pk %}" method="POST">
        {% csrf_token %}
        <button>삭제하기</button>
    </form>
    {% endblock content %}
    ```
    
3. 사용자가 입력한 데이터를 전송받아  BD에 저장하는 함수 1개
    - urls.py
    
    ```python
    # articles/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        path('update/<post_id>/', views.update, name='update'),
    ]
    ```
    
    - views.py
    
    ```python
    # articles/view.py
    
    from django.shortcuts import render, redirect
    from .models import Post
    
    def update(request, post_id):
        # 1. 수정할 글 데이터를 찾아온다.
        post = Post.objects.get(pk=post_id)
        # 2. 수정한다.
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        # 3. 저장한다.
        post.save()
        # 4. 글 수정 완료되었으니 글 디테일 페이지로 가서 글 확인하도록 
        return redirect('articles:detail', post.pk)
    ```
    
    - templates/edit.html
    
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1>글 수정하기</h1>
    {% comment %} 수정정보를 articles/views.py update함수에 전달 {% endcomment %}
    **<form action="{% url 'articles:update' post.pk %}" method="POST">**
        {% csrf_token %}
        <label for="title" >글 제목</label>
        {% comment %} 기존의 값을 보여줘야 한다. {% endcomment %}
        <input type="text" id="title" name="title" value="{{post.title}}"><br>
        <label for="content" id="content" name="content">글 내용</label>
        {% comment %} textarea 태그는 value속성이 없으므로 태그 내부 값으로 작성 {% endcomment %}
        <textarea name="content" id="content" cols="30" rows="10" >{{post.content}}</textarea><br>
        <button>글쓰기</button>
    </form>
    
    {% endblock content %}
    ```
    

---

# Admin site

- Django의 automatic admin interface
- “관리자 페이지”
    - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
    - 모델 class를 admin.py에 등록하고 관리
    - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드 삽입도 가능
- `$ python manage.py createsuperuser`
    - username과 password를 입력해 관리자 계정을 생성(email은 선택사항)
- 접속 주소 : https://127.0.0.1:8000/admin/
- 모델의 레코드 보기
    
    ```python
    # articles/admin.py
    
    from django.contrib import admin
    from .models import Article
    
    admin.site.register(Article)
    ```
    

---

# 요약

1. Model
    - Django는 Model을 통해 데이터에 접속하고 관리
2. ORM
    - 객체지향 프로그래밍을 이용한 DB 조작
3. Migrations
    - 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법
4.  HTTP request&response
    - 요청에 행동을 표현하는 HTTP request method
    - 요청에 대한 성공 여부 응답을 숫자로 표현하는  HTTP response status codes

---

추가 설치

- VScode
    - SQlite
        - db.splite3 우클릭 - open database
        - vscode 왼쪽하단 sqlite explorer 확인