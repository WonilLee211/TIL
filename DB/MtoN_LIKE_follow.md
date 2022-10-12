# M:N (article_user) like service

# 1.LIKE

## 1.1 모델 관계 설정

- ManyToManyField 작성
- 이 게시글에 좋아요를 누른 유저

```python
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
```

- 에러발생
  - `user필드와 like_user 필드로 역참조할 때 충돌 !(.article_set 매니저)`
  - related_name 필수적이다.
  - 이런 경우 보통 M:N을 related_name 지정함

```python
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
...
```

### User-Article 간 사용가능한 related_manager 정리

- article.user
  - 게시글을 작성한 유저-N:1
- user.article_set
  - 유저가 작성한 게시글(역참조) - N:1
- article.like_users
  - 게시글을 좋아요한 유저 - M:N
- user.like_articles
  - 유저가 좋아요한 게시글(역참조) - M:N

## 1.2 구현

- urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
...
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

- views.py

```python
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 좋아요를 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
    # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지 확인
    # if request.user in article.like_users.all():

    # 현재 게시글에 좋아요를 누른 유저 중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```

- index.html

```python
{% extends 'base.html' %}

{% block content %}
...
    <div>
      <form action="{% url 'articles:likes' article.pk %}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소">
        {% else %}
          <input type="submit" value="좋아요">
        {% endif %}
      </form>
    </div>
...
{% endblock content %}
```

### . exists()

- QuerySet에 결과가 포함되어있으면 True를 반환하고 그렇지않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

# M:N(User-User)

- User자기 자신과의 M:N관계 설정을 통한 `팔로우 기능 구현`

# 1. Profile

- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성
- urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
...
    path('profile.<str:username>/', views.profile, name='profile'),
]
```

```python
# views.py
def profile(request, username):
    person = get_object_or_404(User, username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)
```

>  [주의]
> 
> path(’<str:username>’, viwes.profile, name=’profile’)
> 
> 위처럼 작성하면 모든 문자열 주소가 저기로 간다! 주의
> 
> accounts/profile.html



```python
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}</h1>
<h2>작성한 게시글 목록</h2>
{% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
{% endfor %}

<h2>작성한 댓글 목록</h2>
{% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
{% endfor %}

<h2>좋아요한 게시글 목록</h2>
{% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>

{% endfor %}

{% endblock content %}
```

- 프로필로 이동할 수 있는 탬플릿으로 이동 하이퍼링크 작성
  
  - base.html
    
    ```python
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
      {% if request.user.is_authenticated %}
        <h3>{{ user }}</h3>
        <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
        <form action="{% url 'accounts:logout' %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="Logout">
        </form>
      ...
    
    </div>
    
    </body>
    </html>
    ```
  
  - articles/index.html
    
    ```python
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>Articles</h1>
    {% if request.user.is_authenticated %}
      <a href="{% url 'articles:create' %}">CREATE</a>
    {% endif %}
    <hr>
    {% for article in articles %}
      <p>
        <b>작성자 : <a href="{% url 'accounts:proflie' article.user.username %}">{{ article.user }}</a></b>
      </p>
      <p>글 번호 : {{ article.pk }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <div>
    ...
    {% endblock content %}
    ```

## 2. Follow

### 2.1 모델 관계 설정

- ManyToManyField 작성 및 Migration 진행

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name = 'followers')
```

### 2.2 구현

- accounts/urls.py
  
  ```python
  ...
  app_name = 'accounts'
  urlpatterns = [
  ...
      path('<int:user_pk>/follow/', views.follow, name='follow'),
  
  ]
  ```

- accounts/views.py
  
  ```python
  def follow(request, user_pk):
      User = get_user_model()
      me = request.user
      you = User.objects.get(pk=user_pk)
      if me != you:
          # if me in you.followers.all():
          if you.followers.filter(pk=me.pk).exists():
              you.followers.remove(me)
          else:
              you.followers.add(me)
      return redirect('accounts:profile', you.username)
  ```

- 프로필 유저의 팔로잉, 팔로워 수& 팔로우,언팔로우 작성

```python
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>
<div>
    <div>
        팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all | length }}
    </div>
    {% if request.user != person %}
        <div>
            <form action="{% url 'accounts:follow' person.pk %}" method="POST">
                {% csrf_token %}
                {% if request.user in person.followers.all %}
                    <input type="submit" value="unfollow">
                    {% else %}
                    <input type="submit" value="follow">
                {% endif %}
            </form>
        </div>
    {% endif %}
</div>
...
{% endblock content %}
```

- 데코레이터 및 is_authenticated 추가

```python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:

        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            # if me in you.followers.all():
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('account:login')
```

### with template tag

https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#with

- 더 간단한 이름으로 복잡한 변수를 저장한다.
- 주로 데이터베이스에 중복으로 여러번 엑세스 할 때 유용하게 사용한다.
- 변수는 {% with %} and {% endwith %} 사이에서만 사용 가능하다.

```django
<!-- accounts/profile.html -->

{% with followings=person.followings.all followers=person.followers.all %}
  <div> 
    <div>
      팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in followers %}
            <button>Unfollow</button>
          {% else %}
            <button>Follow</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
{% endwith %}
```