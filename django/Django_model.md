# Django Model
- Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

## - DATABASE
- 체계화된 데이터의 모임
- 검색 및 구조화 작업을 쉽게 수행하기 위해 조직화된 데이터를 수집 저장하는 시스템

## -   1. DB 기본구조
1. 스키마(schema)
2. 테이블(table)

### 1.1 스키마(Schema)

- 뼈대(Structure)
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

|column|datatype|
|---|---|
|id|INT|
|name|TEXT|
|age|INT|
|email|TEXT|

### 1.2 테이블(Table)

- 필드와 레코드를 사용하여 조직된 데이터 요소들의 집합
- 관계라고도 부르기도 함
1. 필드(field)
    - 속성, 컬럼
    - 각 필드에서는 고유한 데이터 형식이 지정됨(INT, TEXT 등)
2. 레코드(record)
    - 튜플, 행
    - 테이블의 데이터는 레코드에 저장됨

### 1.3 PK(Primary Key)
- 기본 키
- 각 레코드의 고유한 값(식별자로 사용)
- `다른 항목과 절대로 중복될 수 없는 단일값(unique)`
- 데이터베이스 관리 및 테이블간 관계설정 시 주요하게 활용됨
- 예시>  주민등록번호

### 1.4 쿼리(Query)
- **데이터**를 **조회**하기 위한 명령어
- 주로 테이블 형 자료 구조에서 조건에 맞는 데이터를 추출하거나 조작하는 명령어
- Query를 날린다.
    - 데이터베이스를 조작한다 !
    
---
## - 2. Model

- Django가 데이터에 접근하고 조작하는 도구
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 일반적으로 각각의 모델은 하나의 DB테이블에 매핑
    - 모델 클래스 1개 == DB 테이블 1개
    

## 모델 작성하기 - 새 프로젝트

### -  Schema 만들기

- models.py 작성
    - 모델 클래스를 작성하는 것은 **DB 테이블 스키마를 지정**하는 것
    - “모델 클래스 == 테이블 스키마”
    
    ```python
    # articles/model.py
    from django.db import models

    class Article(models.Model):
        title = models.CharField(max_length=10) # 클래스변수 title과 content는 DB 필드 나타냄
        content = models.TextField() # 클래스 변수 = 클래스 변수 값
    ```
    
    - 각 모델은 django.models.Model 클래스의 서브 클래스로 표현
        - 즉, 각 모델은 Django.db.models 모듈의 model클래스를 상속받아 구성됨
        - 클래스 상속 기반 형태의  Django 프레임워크 개발
    - models 모듈을 통해 어떠한 타입의  DB 필드(컬럼)을 정의할 것인지 정의
        - 클래스변수 title과 content는 DB 필드 나타냄
    - 클래스 변수(속성) 명 : Title, content
    - 클래스 변수 값( models 모듈의  field클래스
        - DB필드의 데이터 타입

### - Django model Field

- 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형(INT, TEXT)을 정의
- 데이터 유형에 따라 다양한 모델 필드를 제공
    - DataField(), CharField(), IntegerField() 등
    - http://docs.djangoproject.com/en/3.2/ref/models/fields

### - 사용한 모델 필드 알아보기

- **CharField(max_length-None, **options)**
    - 길이의 제한이 있는 문자열 넣을 때 사용
    - max_length
        - 필드의 최대 길이(문자)
        - **CharField의 필수 인자**
        - db와 django의 **유효성 검사(값을 검증)에서 활용**됨
- **TextField(**options)**
    - 글자의 수가 많을 때 사용
    - max_length 옵션 작성 시 사용자 입력단계에서 반영
    - 모델과 BD단계에 적용되지 않음(CharField를 사용해야 함)
        - 실제로 저장할 떄 길이에 대한 유효성 검증하지 않음
    

### 데이터베이스 스키마

- 지금까지 작성한 models.py

|column|data type|
|---|---|
|title|VARCHAR(10)|
|content|TEXT|
- 이제 DB에 테이블을 생성하기 위한 필요함
---
## - 3. Migration

- **주요 명령어**
    1. makemigraion
    2. migrate
    
### - makemigrations
- `python manage.py makemigrations`
- 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도, 청사진 이하 마이그레이션)을 만들 때 사용
- “테이블을 만들기 위한 설계도를 생성하는 것”
- 명령어 실행 후 migrations/0001_initial.py가 생성된 것을 확인
- **‘파이썬으로 작성된 설계도’**

### - migrate
- `python manage.py migrate`
- makemigrations로 만든 설계도를 실제 db.sqlite3 db파일에 반영하는 과정
- 결과적으로 모델에서의 변경사항들과 db의 스키마가 동기화를 이룸
    - `모델과 db의 동기화`
- 설계도(migration)를 실제 db.sqlite3 db파일에 반영

### - 참고 migrations 기타 명령어

1. showmigrations
    1. `python manage.py showmigrations`
    2. migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인
    3. [x]표시가 있으면 migrate가 완료되었음을 의미
2. sqlmigrate
    1. `python manage.py sqlmigrate articles 0001`
    2. 해당 migrations 파일이  sql문으로 어떻게 해석될지 미리 확인
    
--- 
## - 4. ORM(Object-Relational-Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템(Django ↔SQL)간에 데이터를 변환하는 프로그래밍 기술
- 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터 베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용

### — ORM 장점

- SQL을 잘 몰라도 객체지향 언어로 DB 조작이 가능
- 객체 지향적 접근으로 인해 **높은 생산성**

### — ORM 단점

- ORM만으로 완전한 서비스를 구현하기 어려운 경우
---
## - 5. 추가 필드 정의

### model 변경사항 반영하기
- 모델 필드(컬럼) 추가
- model.py에 변경사항이 생겼을 때
  -  `$ python manage.py makemigrations`
    ```python
    # articles/models.py
    from django.db import models

    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
  ```

- 컬럼은 빈 값으로 추가될 수 없음
- 추가되는 컬럼에 대한 기본값을 설정하는 과정
  - 각 보기 번호의 의미
    1. 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력하는 방법
    2. 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법
  - 1번 입력 후 enter(추가된 필드의 default값 설정)
  - 다음 화면에서 enter
    - 기본적으로 django에서 파이썬의 timezone모듈의 now메서드 반환 값을 기본값으로 설정
  - 새로운 설계도 생성 완료
  - DB와 동기화 : `$ python manage.py migrate`


### <mark> 반드시 기억해야 할 migration 3단계</mark>

1. models .py에서 변경사항 발생
2. migrations 파일 생성(설계도 생성)
    - makemigrations
3. DB 반영(모델과 DB의 동기화)
    - migrate

### <mark> DateTimeField()</mark>

- python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
- DateField를 상속받는 클래스
- 선택인자
    1. `auto_now_add`
        - 최소생성일자(useful for creation of timestamps)
        - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
            - 테이블에 어떤 값을 최초로 넣을 때
    2. `auto_now`
        - 최종 수정 일자(useful for “last-modified” of timestamps)
        - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

---
