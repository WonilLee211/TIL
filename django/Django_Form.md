# Django Form

## 개요

- 고객의 요청 중에 비정상적이거나 악의적인 요청을 거르기 위해 `유효성 검증이 필요`
    - 개발 생산성을 늦추는 작업
- **Django Form**
    - 과중한 작업과 반복코드를 줄여줌으로써 쉽게 유효성 검증을 진행할 수 있도록 함

### Form에 대한 Django의 역할

- 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공
- **Django의 Form 관련 처리  3가지**
    1. 렌더링을 위한 데이터 준비 및 재구성
    2. 데이터에 대한 HTML forms 생성
    3. 클라이언트로 받은 데이터 수신 및 처리

## - 1. The Django Form Class

### 1.1 Form class

- Django form 관리 시스템의 핵심

### 1.2 Form Class 선언

- Model Class를 선언하는 것과 비슷
- Model과 마찬가지로 상속을 통해 선언(`from forms import Form`)
- 앱 폴더에 forms.py를 생성 후 ArticleForm Class 선언
    
    ```python
    # articles/forms.py
    
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length = 10)
        content = forms.CharField()
    ```
    
    - form : `TextField` 없음
    - 더 나은 유지 보수 및 관행적 관점에서 forms.py 파일 안에 작성하는 것을 권장
- ‘new’ view함수 업데이트
    
    ```python
    # articles/views.py
    
    from .forms import AricleForm
    
    def new(request):
        form = ArticleForm() # form
        context = {
            'form':form,
        }
        return render(request, 'articles/new.html', context)
    ```
    
- ‘new’ template 업데이트 (`{{form.as_p}}` 추가)
    
    ```html
    <!-- ariticles/new.html -->
    
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>NEW</h1>
      <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        **{{form.as_p}}** # 사용자 정보 입력창이 한줄로 바뀜
    
      </form>
      <hr>
      <a href="{% url 'articles:index' %}">뒤로가기</a>
    {% endblock content %}
    ```
    

- view함수에서 정의한 articleForm의 인스턴스(form) 하나로 input과 label 태그가 모두 렌더링 된다 !
    
    
- 각 태그의 속성값 자동 설정됨

### 1.3 Form rendering options

- `<label>` & `<input>` 쌍에 대한 3가지 출력 옵션
    1. **as_p()**
        - 각 필드가 단락(<p>태그)으로 감싸져서 렌더링
    2. as_ul()
    3. as_table()

### 1.4 django의 2가지 HTML input 요소 표현

1. Form field
    - 입력에 대한 유효성 검사 로직 처리
    
    ```python
    # 예시
    forms.CharField()
    ```
    
    - 탬플릿에서 직접 사용
2. **Widgets**
    - 웹 페이지의 HTML input 요소 렌더링을 담당
        - input 요소의 단순한 출력부분을 담당
        
        ```python
        # 예시
        
        forms.CharField(widget=forms.Textarea)
        ```
        
    - 반드시 `form fields` 에 할당됨

## - 2. Widgets

- Django의 HTML input element 표현을 담당
- 웹페이지에서 input element의 HTML 렌더링을 처리하는 것
    - 유효성 검증과 아무런 관계가 없음

### 2.1 Textarea 위젯 적용

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length = 10)
    content = forms.charField**(widget=forms.Textarea)**
```

### 2.2 Form field와 widget 응용하기

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    Nation_A = 'kr'
    Nation_B = 'ch'
    Nation_C = 'jp'

    NATIONS_CHOICES = [
        (Nation_A, '한국'),
        (Nation_B, '중국'),
        (Nation_C, '일본'),
    ]

    title = forms.CharField(max_length = 10)
    content = forms.charField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices=NATIONS_CHOICES)
    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
```

<h4><참고> 다양한 built-in 위젯 : https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets

</h4>