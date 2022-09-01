# QuerySet API

## - 1. 외부라이브러리 설치 및 설정

```bash
$ pip install ipython django-extentions
```

```python
# settings.py

INSTALLED_APP = [
    'articles',
    'django_extensions',
    ...,
]
```

- 패키지 목록 업뎃
- `$ pip freeze > requirements.txt`

### 참고

- **iPython**
    - 파이썬 기본 쉘보다 더 강력한 파이썬 쉘
    - Django-extensions
- **django-extensions**
    - Django 확장 프로그램 모음
    - shell_plus, graph model 등 다양한 확장 기능 제공
    - 
- **shell**
    - 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
    - 셀은 사용자와 운영체제의 내부 사이의 인터페이스를 감싸는 층이기 때문에 그러한 이름이 붙음
    - “사용자↔shell↔운영체제”
- **python Shell**
    - 파이썬 코드를 실행시켜주는 인터프리터
        - 인터프리터 : 코드를 한 줄씩 읽어 내려가며 실행하는 프로그램
    - 인터렉티드 or 대화형 shell이라고 부름
    - python 명령어를 실행하여 그 결과는 바로 제공
    - `# python -i`
- Django shell
    - ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
    - 파이썬 쉘을 통해서 장고프로젝트에 영향을 줄 수 없기 때문에 Django shell  사용
    - `$ python manage.py shell_plus` : shell 보다 강력한 shell_plus 사용
    
## - 2. QuerySet API

### DB API

- 장고가 기본적으로 ORM을 제공함에 따른 것으로 DB 조작을 편하도록 도움
- Model을 만들면 장고는 객체들을 만들고 읽고 수정하고 지울 수 있는 DB API를 자동으로 만듦
- **구문**
    - `Article.objects.all()` : (model class).(manager).(Queryset API)

### “objects” manager

- “DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager”
- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
- 장고는 기본적으로 모든 장고 모델 클래스에 대해 objects라는 manager 객체를 자동으로 추가함
- 이 manager(objects)를 통해 특정 데이터를 조작(method)할 수 있음

### Query

- 데이터베이스에 특정한 데이터를 보여달라는 요청
    - 쿼리문을 작성한다 → 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드 작성
- 이 때, 파이썬으로 작성한 코드가 ORM에 의해 변환되어 데이터베이스에 전달
    - DB 응답은 ORM이 `QuerySet`  이라는 자료형태로 변환
    

### QuerySet

- 데이터베이스에게서 전달받은 객체 목록
    - **순회가 가능한 데이터**
    - 1개 이상의 데이터를 불러와 사용 가능
- 장고 ORM을 통해 만들어진 자료형(필터나 정렬 작업 가능)
- “object”  manager를 사용하여 복수의 데이터를 가져오는 Queryset method를 사용할 때 반환되는 객체
- 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌, 모델(class)의 인스턴스로 반환됨

---

# QuerySet API 익히기

- 데이터 생성, 읽기, 수정, 삭제

## - CRUD

- Create/ Read/ Update/ Delete
    - 생성/ 조회/ 수정/ 삭제

## - 1. CREATE

### 데이터 객체를 생성하는 방법 1st

1. article = Article()
    - 클래스를 통한 인스턴스 생성
2. article.title
    - 클래스 변수명과 같은 이름의 인스턴스 변수 생성 후 값 할당
3. article.save()
    - 인스턴스로 save메서드 호출
    
    ```bash
    >>> article = Aricle()
    >>> article.title = 'django'
    >>> article.save()
    >>> article.pk
    1 # django가 제공하는 shortcut 때문에 pk 사용 가능
    ```
    
- `article.create_at` : 생성날짜 반환

### 데이터 객체를 생성하는 방법 2nd

- 인스턴스 생성 시 초기값을 함께 작성
    
    ```bash
    >>> article = Article(title='second', content='django!')
    >>> article.save()
    ```
    

### 데이터 객체를 생성하는 방법 3rd

- QuerySet API 중 create() 메서드 활용
    
    ```bash
    >>> Article.objects.create(title='third', content='django')
    <Aritcle:Article object (3)>
    ```
    

### - .save()

- 객체를 데이터베이스에 저장
- 단순히 모델 클래스를 통해 인스턴스 생성하는 것은 DB에 영향을 끼치지 않음
    - 반드시 save 호출해야 테이블에 record 생성됨

## - 2. READ

- 종류
    1. return new querysets
    2. do not return querysets

### all()

- QuerySet return
- 전체 데이터 조회
    
    ```bash
    >>> Article.objects.all()
    <QuerySet [<Article: Article object(1)>, <Article: Article object(2)>, <Article: Article object(3)>]>
    ```
    

### get()

- **단일 데이터 조회**
- 객체를 찾을 수 없다면, raise `DoesNotExist`
- 둘 이상의 객체를 찾고 있으면, raise `MultiObjectsReturne`
- <mark>고유성(uniqueness)을 보장하는 조회에서 사용해야 함</mark>

### filter(매개변수= 값)

- 지정된 조회 **매개 변수와 일치하는 객체를 포함한 새 QuerySet**을 반환(없어도 반환)

```bash
>>> Article.objects.filter(content='??')
<QuerySet []>
```

### Field lookups

- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨

```bash
# field lookups 예시
# "content 컬럼에 'dj'가 포함된 모든 데이터 조회"
Article.objects.filter(content__contains='dj')
```

- 참조 : https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

## - 3. UPDATE

- update 과정
    1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
    2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
    3. save() 인스턴스 메서드 호출
        
        ```bash
        >>> article = Article.objects.get(pk=1)
        # 인스턴스 변수를 변경
        >>> article.title = 'byebye'
        
        # 저장
        >>> article.save()
        
        # 정상적으로 변경된 것을 확인
        >>> article.title
        'byebye'
        ```
        

## - 4. DELETE

1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. delete() 인스턴스 메서드 호출
    
    ```bash
    >>> article = Article.objects.get(pk=1)
    # delete 메서드 호출
    >>> article.delete()
    (1, {'articles.Article':1})
    
    # 1번 데이터는 이제 조회할 수 없음
    >>> Article.objects.get(pk=1)
    DoesNotExist: Article matching query does not exist
    ```
    

### 참고 __str__()

- 표준 파이썬 클래스의 메서드인 str()
- 각각의 object가 사람이 읽을 수 있는 문자열을 반환

```python
# models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

- Django shell에서 변화된 출력 확인

```bash
>>> article = Article.objects.get(pk=1)
>>> article
<QuerySet [<article: 'first']>
```