# QuerySet API Advanced

## 초기 설정

1. 가상환경 생성 및 활성화
2. 패키지 목록 설치
3. migrage 진행
4. sqlite3에서 csv 데이터 import 하기
    - `$ sqlite3 db.sqlite3`
    - `sqlite >  .mode csv`
    - `sqlite >  .import users.csv users_user`
    - `sqlite >  .exit`

## 1. CRUD 기본

### 1.1 모든 user 레코드 조회
- `User.objects.all()`

### 1.2 user 레코드 생성

```bash
User.objects.create(
...: first_name='길동',
...: last_name='홍',
...: age=100,
...: country='제주도',
...: phone='010-1234-5678',
...: balance=10000,)
Out[3]: <User: User object (101)>
```

### 1.3 101번 user 레코드 조회

```bash
User.objects.get(pk=101)
```

### 1.4 101번 user 레코드의 last_name을 김으로 수정

```bash
user = User.objects.get(pk=101)

In [5]: user.last_name='김'

In [6]: user.save()

```

### 1.5 101번 삭제

```bash
user = User.objects.get(pk=101)
user.delete()

```

### 1.6 전체 인원수 조회_ count()

```bash
# len(User.objects.all())

User.objects.count()
```

### - .count()

- QuerySet과 일치하는 데이터베이스의 개체 수를 나타내는 정수를 반환
- .all() 사용하지 않아도 됨


## 2. sorting data

### 2.1 나이가 어린 순으로 이름과 나이 조회

```bash
User.objects.order_by('age').values('first_name', 'age')
```

### - order_by()

- .order_by(*fields)
- QuerySet의 정렬을 재정의
- 기본적으로 오름차순으로 정렬하며 필드명에 ‘-’(하이픈)을 작성하면 내림차순으로 정렬
    - `User.objects.order_by('-age').values('first_name', 'age')`
- 인자로 ‘?’를 입력하면 랜덤으로 정렬
    - `User.objects.order_by('?').values('first_name', 'age')`

### - values()

- .values(*fields, **expressions)
- 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
- *fields는 선택인자이며 조회하고자하는 필드명을 가변인자로 입력받음
    - 필드 지정 : 각 딕셔너리에는 지정한 필드에 대한 key:value만을 출력
    - 필드 미지정 : 각 딕셔너리에 레코드의 모든 필드에 대한 key:value 출력

### 2.2 이름과 나이를 나이가 많은 순서대로 조회

```bash
User.objects.order_by('-age').values('first_name', 'age')

```

### 2.3 이름, 나이, 계좌 잔고를 나이가 어린 순으로 만약 같은 나이라면 계좌잔고가 많은 순으로 정렬해서 조회

```bash
User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance')
```

### 주의

```bash
User.objects.order_by('age').order_by('-balance')
# 결국 User.objects.order_by('-age')와 같다.
```

## 3. Filtering data

### 3.1 중복없이 모든 지역 조회하기

```bash
User.objects.distinct().values('country')
```

### 3.2 지역순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기

```bash
User.objects.distinct().values('country').order_by('country')
```
 
### 3.3 이름과 지역이 중복없이 모든 이름과 지역 조회하기

```bash
User.objects.distinct().values('first_name', 'country')
```

### 3.4 이름과 지역이 중복없이 지역순으로 오름차순 정렬하여 모든 이름과 지역조회하기

```bash
User.objects.distinct().values('first_name', 'country').order_by('country')
```

### 3.5 나이가 30인 사람들의 이름 조회

```bash
User.objects.filter(age=30).values('first_name')
```

### 3.6 나이가 30살 이상인 사람들의 이름과 나이 조회하기

```bash
User.objects.filter(age__gte = 30).values('first_name', 'age')

```
- __gte : greater than equal

### - Field lookups

- SQL WHERE절에 상세한 조건을 지정하는 방법
- QuerySet메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 사용됨
- 문법 규칙
    - 필드명 뒤에 ‘double-underscore’ 이후 작성함
    - `field__lookuptype=value`
- https://docs.djangoproject.com/en/3.2/ref/models/querysets/-field-lookups

### 3.7 나이가 30살 이상이고 계좌 잔고가 50만원 초과인  사람들의 이름, 나이, 계좌 잔고 조회하기

```bash
User.objects.filter(age__gte=30, balance__gt=500000).values('first_name', 'age', 'balance')
```

### 3.8 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회

```bash
User.objects.filter(first_name__contains='호').values('first_name', 'last_name')

```

### 3.9 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회

```bash
User.objects.filter(phone__startswith='011-').values('first_name', 'phone')
```

- SQL에서의 ‘%’ 와일드 카드와 같음
- ‘_’(under score)는 별도로 정규 표현식을 사용해야 함

### 3.10 이름이 ‘준’으로 끝나는 사람들의 이름 조회하기

```bash
User.objects.filter(first_name__endswith='준').values('first_name')
```

### 3.11 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기

```bash
User.objects.filter(country__in=['강원도', '경기도']).values('first_name', 'country')
```

### 3.12 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회

```bash
User.objects.exclude(country__in=['경기도', '강원도']).values('first_name', 'country')
```

### 3.13 나이가 30이거나 성이 김씨인 사람들 조회(중요)

```bash
from django.db.models import Q
User.objects.filter(Q(age=30) | Q('last_name'='김')
```

### - ‘Q’ objects

- 기본적으로 fliter()와 같은 메서드의 키워드 인자는 AND statement를 따름
- 만약 `더 복잡한 쿼리를 실행해야 하는 경우`가 있다면 `Q객체가 필요함`
    - 예를 들어 OR statement 같은 경우
    
    ```bash
    # 예시
    from django.db.models import Q
    Q(question__startswith='What')
    ```
    
    - ‘&’ 및 ‘|’를 사용하여 `Q 객체를 결합할 수 있음`
    
    ```bash
    # 예시
    Q(question__startswith='who') | Q(question__startswith='what')
    ```
    
    - 조회를 하면서 여러 Q객체를 제공할 수도 있음
    
    ```bash
    Article.objects.get(
        Q(title__startswith='who'),
        Q(create_at=date(2005, 5, 2)) | Q(create_at=date(2005, 5, 6))
    ```



## 4. Aaggregation(Grouping data)

## 4.1 aggregate()

- 전체 queryset에 대한 값을 계산
- `특정 필드 전체의 합, 평균, 개수 등을 계산`할 때 사용
- 딕셔너리를 반환
- **functions**
    - Avg, Count, Max, Min, Sum 등

### 4.1.2 나이가 30살 이상인 사람들의 평균 나이 조회하기

```bash
# shell_plus에서는 import하지 않아도 된다.
from django.db.models import Avg

User.objects.filter(age__gte=30).aggregate(Avg('age'))
# 딕셔너리 key 이름 수정
User.objects.filter(age__gte=30).aggregate(avg_value=Avg('age'))
```

### 4.1.3 가장 높은 계좌 잔액 조회

```bash
from django.db.models import Max
User.objects.aggregate(Max('balance'))
```

### 4.1.4 모든 계좌 잔액 총액 조회

```bash
from django.db.models import Sum

User.objects.aggregate(Sum('balance'))

```

## 4.2 annotate()

- 쿼리의 각 항목에 대한 요약 값을 계산
- SQL의 GROUP BY에 해당
- ‘주석을 달다’라는 사전적 의미
 
### 4.2.1 각 지역별로 몇 명씩 살고 있는지 조회

```bash
from django.db.models import Count
User.objects.values('country').annotate(Count('country'))

'''
<QuerySet [{'country': '강원도', 'country__count': 14}, {'country': '경
기도', 'country__count': 9}, {'country': '경상남도', 'country__count': 9}, {'country': '경상북도', 'country__count': 15}, {'country': '전라남도', 'country__count': 10}, {'country': '전라북도', 'country__count': 11}, {'country': '제주도', 'country__count': 1}, {'country': '제주특별자치도', 'country__count': 9}, {'country': 
'충청남도', 'country__count': 9}, {'country': '충청북도', 'country__count': 14}]>
'''

User.objects.values('country').annotate(num_of_country=Count('country'))
```

### 4.2.2 각 지역별로 몇 명씩 살고 있는지 + 지역별 계좌 잔액 편균 조회하기

- 한번에 여러 값을 계산해 조회할 수 있음

```bash
User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))

<QuerySet [{'country': '강원도', 'country__count': 14, 'avg_balance': 157895.0}, {'country': '경기도', 'country__count': 9, 'avg_balance': 182852.22222222222}, {'country': '경상남도', 'country__count': 9, 'avg_balance': 73870.0}, {'country': '경상북도', 'country__count': 15, 'avg_balance': 75630.0}, {'country': ' 
전라남도', 'country__count': 10, 'avg_balance': 66265.0}, {'country': '전라북도', 'country__count': 11, 'avg_balance': 161138.18181818182}, {'country': '제주도', 
'country__count': 1, 'avg_balance': 10000.0}, {'country': '제주특별자치도', 'country__count': 9, 'avg_balance': 351233.3333333333}, {'country': '충청남도', 'country__count': 9, 'avg_balance': 104304.44444444444}, {'country': '충청북도', 'country__count': 14, 'avg_balance': 159610.7142857143}]>
```

### 4.2.3 각 성씨가 몇 명씩 있는지 조회하기
```bash
from django.db.models import Count
User.objects.values('last_name').annotate(Count('last_name'))

```

### 4.2.4 N:1 예시(중요)

- 만약 Comment-Article 관계가 N:1인 경우

```bash
# 예시
Article.objects.annotate(
    number_of_comment=Count('comment'),
    pub_date=Count('comment', filter=Q(comment__create_at__lte='2000-01-01'))
)
```


- 전체 게시글을 조회하면서(Article.objects.all())
- annotate로 각 게시글의 댓글 개수(number_of_comment)와
- 2000-01-01보다 나중에 작성된 댓글의 수(pub_date)를 함께 조회하는 것
```bash
Article.objects.annotate(
    number_of_comment=Count('모델명(단수형)'),
    pub_date=Count('모델명(단수형)', filter=Q((모델명단수형)__필드명__lte='2000-01-01'))
)

```