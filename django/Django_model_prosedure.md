# Model 기본 진행 방식
1. `models.py` 에 클래스를 정의한다.
    1. 이 때 클래스는 models.Model 을 상속 받아서 작성한다.
    2. 필요한 필드를 구성한다.
    3. 예시 코드
        
        ```python
        class Post(models.Model):
            # CharField / TextField 문자를 저장하기 위한 필드
            # CharField : 글자 제한 / Textfield : 글자 제한이 없을 때 사용
            title = models.CharField(max_length=255)  
            content = models.TextField()
        ```
        

1. 작성 완료 되었으면 DB에 적용시켜야 하는데
    1. 가장 먼저 설계도를 만들어야 한다.
        1. `python manage.py makemigrations`
    2. 설계도 생성이 되었으면 이제 DB에 적용시켜줘야 한다.
        1. `python manage.py migrate`
        
2. CREATE (3가지 방법이 존재)
    1. 빈 인스턴스 생성하는 방법
    2. 인스턴스 생성할 때 값을 주는 방법
    3. Queryset API 의 create 사용하는 방법

1. READ
    1. 전체 데이터를 읽어 오는 방법
    2. 단일 데이터를 읽어 오는 방법
        1. 어떤 글에 대한 정보를 가져오는지 글 정보를 variable routing으로 전달되어야 한다.
    
2. UPDATE
    1. 데이터를 수정하는 방법
        1. DB에서 수정할 데이터를 가져온다.
        2. 수정한다
        3. 저장한다
    2. 데이터를 수정하기 위해 필요한 정보
        1. 어떤 데이터를 수정하는지 데이터의 pk 값
        2. 클릭했을 때 해당 글의 정보를 variable routing 으로 전달해야 한다.

1. DELETE
    1. 데이터를 삭제하는 방법
        1. 삭제할 데이터를 DB에서 가져온다
        2. 삭제한다

1. CRUD의 동작은 다음 페이지 혹은 동작이 어떤 것이 되어야 하는지 고민해 보면서 정리해주세요.