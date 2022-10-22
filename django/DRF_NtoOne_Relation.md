# Django REST framework - N:1 Relation

- N: 1 관계에서의 모델 data를 Serialization하여 Json으로 변환하는 방법 학습

## 사전준비

- Comment 모델 작성 및 DB 초기화
- migration 진행
- fixtures 데이터 로드
    - `$ python manage.py loaddata articles.json comments.json`
    

# 1. GET- LIST

- 댓글 데이터 목록 조회하기
- Article List와 비교하며 작성해보기

```python
# articles/serializers.py
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
```

```python
from django.urls import path
from . import views

urlpatterns = [
,,,
    path('comments/', views.comment_list),
]
```

```python
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
```

- 단일 댓글 조회하기(같은 시리얼라이저 사용)

```python
from django.urls import path
from . import views

urlpatterns = [
...
    path('comments/<int:article_pk>/', views.comment_detail),
]
```

```python
@api_view(["GET", "DELETE", "PUT"])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
```

# 2. POST

- 단일 댓글 데이터 생성하기
- 역할과 목적이 달라서 url과 view 하나 더 만들기

```python
from django.urls import path
from . import views

urlpatterns = [
...
    path('articles/<int:article_pk>/comments/', views.comment_create),
    
]
```

## 2.1 Passing additional attributes to `.save()`

- 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- CommentSerializer를 통해  serialize되는 과정에서 parameter로 넘어온 article_pk에 해당하는 article 객체를 추가적인 데이터로 넘겨 저장

```python
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk= article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        # form에서 commit=False와의 차이점
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- `에러발생`
- `is_valid에서 article 정보가 빠져있음으로 막힘`
- article field 데이터 또한 사용자로부터 입력받도록 설정되어 있기 때문

## 2.2 읽기 전용 필드 설정

- `read_only_fields`를 사용해 외래 키 필드를 `읽기 전용 필드`로 설정
- **데이터를 전송하는 시점에서 “해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력**

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```

# 3. DELETE & PUT

- 댓글 데이터 삭제 및 수정 구현하기

```python
@api_view(["GET", "DELETE", "PUT"])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        # serializer = ArticleSerializer(instance = article, data=request.data)
        if  serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

# 4. N:1 역참조 데이터 조회(중요)

1. 특정 게시글에 작성된 댓글 목록 출력하기
    - 기존 필드 override
2. 특성 게시글에 작성된 댓글의 개수 출력하기
    - 새로운 필드 추가

### 1번 게시글을 조회하면 댓글을 함께 보내고 싶다 !

## 4.1 특정 게시글에 작성된 댓글 목록 출력하기(override)

- **기존 필드 override** - Article Detail
    - “게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기
    - Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

### 1. PrimaryKeyRelatedField()

```python
class ArticleSerializer(serializers.ModelSerializer):
     # 기존의 related manager 코드명을 오버라이드함
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
```

- **1에서 N을 참조하기 때문에 항상 many=True, read_only=True**
- **역참조하는 대상의 pk 만을 가져옴**
- models.py에서 related_name을 통해 이름 변경 가능
- 역참조 시 생성되는 comment_set을 override할 수 있음

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. Nested relationships

- 더 많은 정보를 담아서 보내기 위한 방법

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
```

- **동작하는 모든 Field의 정보를 가져온다**
- 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩될 수 있음
- 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
- 두 클래스의 상 하 위치를 변경해야 함

## 4.2  특정 게시글에 작성된 댓글의 개수 출력하기(새로운 필드 생성)

- **새로운 필드 추가** - Article Detail
    - ‘게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기’

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
```

- source옵션에 ORM을 작성
    - `Article.comment_set.count()`
    - Article모델 참조하니까 `Article` 생략
    - 문자열이니까 `()` 생략

### `source`

- serializers field’s argument
- 필드를 채우는 데 사용할 속성의 이름
- 점 표기법(dotted notation) 을 사용하여 속성을 탐색할 수 있음

### [주의] 읽기 전용 필드 지정 이슈

- 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않으니 주의
- **기존에 있던 필드만 `read_only_fields` 에 작성 가능**
- 아래 코드는 사용 못함

```python
# 사용 불가능
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count',)
```

# 5. Django Shortcuts functions

- django.shortcuts 패키지는 개발에 도움될 수 있는 여러 함수와 클래스를 제공
- 제공되는 shortcuts 목록
    - `render()`, `redirect()`, `get_object_or_404()`, `get_list_or_404()`
    - https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/

## 5.1 `get_object_or_404()`

- 모델 manager objects에서 get()을 호출하지만 해당 객체가 없을 땐 기존 DoesnotExist예외 대신 Http404를 raise함

```python
article = get_object_or_404(Article, pk = article_pk)
article = get_object_or_404(Article, pk = article_pk)
```

## 5.1 `get_list_or_404()`

- 모델 manager objects에서 filter()의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise함

```python
articles = get_list_or_404(Article)
# articles = Article.objects.all()
comments = get_list_or_404(Comment)
# comments = Comment.objects.all()

```

### 왜 사용?

- 클라이언트 입장에선 서버에서 오류가 발생해서 요청을 수행할 수 없다 (500)라는 원인이 정확하지 않는 에러를 마주하기 보단, 서버가 적절한 예외 처리하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소