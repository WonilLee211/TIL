# Handling HTTP requests

- HTTP requests 처리에 따른 view 함수 구조 변화
- **new-create, edit-update의 view함수 역할**
    - **공통점**
        - new-create : create 로직을 구현하기 위한 공통 목적
        - edit-update : update 로직을 구현하기 위한 공통 목적
    - 차이점
        - new와 edit는 GET요청에 대한 처리만을,
        - create와 update는 POST요청에 대한 처리만은 진행
- **공통점을 합치고 차이점을 구분하여 하나의 함수로 만들자 !**
    - new-create view함수
        
        ```python
        # articles/views.py
        
        def create(request):
            if request.method == 'POST':
                form = ArticleForm(request.POST)
                if form.is_valid():
                    article = form.save()
                    return redirect('articles:detail', article.pk)
            else:
                # new
                form = ArticleForm()
            # 들여쓰기 주의
            context = {
                'form':form,
            }
            return render(request, 'articles/create.html',context)
        ```
        
    - edit-update view함수
        
        ```python
        # articles/views.py
        
        def update(request, pk):
            article = Article.objects.get(pk=pk)
            if request.method == 'POST':
                form = ArticleForm(request.Post, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:detail', article.pk)
        
            else:
                form = ArticleForm(instance=article)
            context = {
                'article': article,
                'form' : form
            }    
        
            return render ('articles/update.html', context)
        ```
        
    - 수정 후 다른 파일에 edit, new 키워드 삭제 & 수정해주기
- delete
    
    ```python
    def delete(request, pk):
        if request.method == "POST":
            article = Article.objects.get(pk=pk)
            article.delete()
            return redirect('articles:index')
    
    ```
    

# View decorators

### 데코레이터(Decortors)

- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- Django는 다양한 HTTP기능을 지원하기 위해 view함수에 적용할 수 있는 여러 데코레이터 제공

### 4.1 Allowed HTTP method

- 데코레이터 사용으로 요청 메서드를 기반으로 접근 제한하기
- 일치하지 않는 메서드 요청이라면 `405 method not allowed` 반환
- 메서드 목록
    1. `require_http_methods()`
    2. `requrie_POST()`
    3. `required_safe()`
- [참고] 405 Method Not Allowed
    - 요청방법이 서버에 전달 되었으나 사용이 불가한 상태

### require_http_methods()

- view함수가 특정한 요청 method만 허용하도록 하는 데코레이터

```python
# views.py

from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def create(request):
    pass

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    pass
```

### require_POST()

- view함수가 POST 요청 method만 허용하도록 하는 데코레이터

```python
# views.py
from django.views.decorators.http import require_http_methods, require_POST

@ require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

- url로 delete 시도 후 로그에 반환값 확인(405 http status code)
    
    ```python
    Method Not Allowed (GET): /articles/3/delete/
    [04/Jan/2022 04:52:10] "GET /articles/3/delete/ HTTP/1.1" 405 0
    ```
    

### **require_safe()**

- require_GET 있지만 Django에서는 require_safe를 사용하는 것을 권장
    
    ```python
    # views.py
    from django.views.decorators.http import require_http_methods, requrie_POST, require_safe
    
    @require_safe
    def index(request):
        ...
    
    @equire_safe
    def detail(request, pk):
        ...
    ```
    

# 마무리

- Django Form Class
    - Django 프로젝트의 주요 유효성 검사 도구
    - 공격 및 데이터 손상에 대한 중요한 방어 수단
    - 유효성 검사에 대해 개발자에 대해 강력한 편의 제공
- view 함수 구조 변화
    - HTTP requests 처리에 따른 구조 변화
    

# Rendering fields manually

- 참고 : working with forms django documentation
- working with form templates 태그 (최하단)

```html
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}

  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>

  <hr>
  <form action="#">
    <div> 
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
  </form>
  <hr>
  <h2>looping over the form's fields</h2>
  <form action="#">
    {% for field in form  %}
      {{ field.title.errors }}
      {{ field.title.label_tag }}
      {{ field.title }}
    {% endfor %}
  </form>

{% endblock content %}
```

## CSS 활용

### bootstrap 사용하기

- form 태그
    - 위젯에 `class = ‘form-control’` 속성을 추가해주기

### 외부라이브러리 적용하기

- v5
    - django-bootstrap-v5.readthdocs.io/en/latest/installation.html
    - 공식문서 따라서 설정해주기

[either.io](http://either.io) 클론코딩