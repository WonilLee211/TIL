# Django REST framework-Single Model

- 단일 모델의 data를 serialization하여 SJON으로 변환하는 방법에 대한 학습

## 사전준비

- postman

# 1. ModelSerializer

- articles/serializers.py 생성
    - serializers.py의 위치나 파일명은 자유롭게 작성 가능

```python
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
```

- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
    1. Model 정보에 맞춰 자동으로 필드를 생성
    2. serializer에 대한 유효성 검사기를 자동으로 생성
    3. .create() 및 .update()의 간단한 기본 구현이 포함됨

## 1.1 serializer 연습하기

- shell_plus 실행 및 ArticleListSerializer import
- `$ python [manage.py](http://manage.py) shell_plus`
- `>>> from articles.serializers import ArticleListSerializer`
- 인스턴스 구조 확인
    - 
    
    ```bash
    serializer = ArticleListSerializer()
    serializer
    ArticleListSerializer():
        id = IntegerField(label='ID', read_only=True)
        title = CharField(max_length=100)
        content = CharField(style={'base_template': 'textarea.html'})
    ```
    
- Model instance 객체 serialize
    
    ```bash
    >>> article = Article.objects.get(pk=1)
    >>> serializer = ArticleListSerializer(article)
    
    ```
    
- Queryset 객체  serialize
    
    ```sql
    
    >>> articles = Article.objects.all()
    >>> serializer = ArticleListSerializer(articles)
    # many=True 옵션 없어서 에러 발생
    >>> serializer.data
    
    # 옵션 추가
    >>> serializer = ArticleListSerializer(articles, many=True)
    >>> serializer.data
    ```
    
    - `many`옵션:  단일 객체 인스턴스 대신 Queryset 또는 객체 목록을 serialize하려면  many=True를 작성해야 함
    - 

# 2. Build RESTful API - Article

## 2.1 GET-List

- 게시글 데이터 목록 조회하기

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
]
```

- `DRF는 api_view 데코레이터 작성은 필수`

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

- 127.0.0.1:8000/api/v1/articles/ 응답 확인

### `api_view` decorator

- DRF view 함수가 응답해야 하는 HTTP 메서드목록을 받음
- 기본적으로 GET메서드만 허용되며 다른 메서드 요청에 대해서는 405 method not allowed로 응답

## 2.2 GET - detail

- 단일 게시글 데이터  조회
- 각 데이터의 상세 정보를 제공하는 ArticleSerializer정의

```python
# article/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

```python
# views.py
@api_view(['GET'])
def article_detail(request, article_pk):
    articles = Article.objects.get(pk = article_pk)
    serializer = ArticleListSerializer(articles)
    return Response(serializer.data)
```

```python
...
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>', views.article_detail),
]
```

## 2.3 POST

- 게시글 데이터 생성하기
- 요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답

```python
# views.py

from rest_framework import status

@api_view(['GET'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
```

### Raising an Exception on invalid data

- `is_valid(raise_exception=True)`
- 유효하지 않은 데이터에 대해 예외 발생시키기
- is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

```python
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
```

## 2.4 DELETE

- 게시글 데이터 삭제하기
- 요청에 대한 데이터 삭제가 성공했을 경우는 204 Not Content 상태코드 응답
- (명령을 수행했고 더 이상 제공할 정보가 없는 경우)

```python
@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    if request.method == "GET":
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## 2.5 PUT

- 게시글 데이터 수정하기
- 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태코드 응답

```python
@api_view(["GET", "DELETE", "PUT"])
def article_detail(request, article_pk):
...
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        # serializer = ArticleSerializer(instance = article, data=request.data)
        if  serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```