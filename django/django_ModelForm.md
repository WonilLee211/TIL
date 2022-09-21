# Django ModelForm

- Model을 통해 Form Class를 만들 수 있는 helper class
- ModelForm은 Form과 똑같은 방식으로 view 함수에서 사용

## -1. ModelFrom 선언

- forms라이브러리에서 파생된 ModelForm 클래스를 상속받음
- 정의한 ModelForm클래스 안에 Meta클래스 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta클래스에 저장

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        # 어떤 모델을 기반으로 할지
        model = Article # 호출(`()`)하지 않음
        # 모델 필드 중 어떤 것을 출럭할지
        fields = '__all__' # 모델에 정의된 모든 fields
```

## -2. ModelForm에서의 Meta Class

- ModelForm의 정보를 작성하는 곳
- 입력된 모델을 참조하여 정의된 field정보를 Form에 적용
    
    ```python
        class Meta:
            model = Article 
            fields = '__all__' 
    ```
    
    ### e**xclude 속성**
    
    - 모델에서 포함하지 않을 필드 지정
    
    ```python
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article 
            exclude = ('title',)
    ```
    

**<참조> 참조값과 반환값**

- 호출하지 않고 이름만 작성하는 방식
    
    ```python
    class ArticleForm(forms.ModelForm):
        class Meta:
            **model = Article** 
            exclude = ('title',)
    ```
    
    - **함수의 `참조값`을 출력 : 참조값을 그대로 넘김으로써, 필요한 시점에 사용하기 위해서**
    
- **주의사항**
    - 지금의 문법을 파이썬 문법으로 접근하지 말 것
    - 그냥 ModelForm의 역할과 사용법을 숙지해야 함
    

## - 2. ModelForm with view functions

### 2.1 CREATE

- 유효성 검사 통과
    - 데이터 저장
    - 상세 페이지로 redirect
- 통과 못하면
    - 작성 페이지로 redirect
    
    ```python
    
    from django.shortcuts import render, redirect
    
    from articles.forms import ArticleForm
    from .models import Article
    
    def create(request):
        form = ArticleForm(request.POST) # form = request.POST.get('..')
        # 사용자 정보 받아서
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
        return redirect('articles:new')
    ```
    

### 2.2 ‘is_valid()’ method

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

### 2.3 form의 인스턴스의 error속성

- is_valid()의 반환값이 False인 경우
    - 유효성 검증 실패한 원인을 딕셔너리 형태로 저장

```python
# aritcles/views.py

from django.shortcuts import render, redirect
from articles.forms import ArticleForm
from .models import Article

def create(request):
    form = ArticleForm(request.POST)
    # 사용자 정보 받아서
    if form.is_valid():
        form.save()
        return redirect('articles:index')
    print(f'에러 : {form.errors}')

    return redirect('articles:new', context)
```

### 2.4 the ‘save’ method

- form 인스턴스의 바인딩된 데이터를 통해 db 객체를 만들고 저장
- ModelForm의 하위 클래스는 **키워드 인자 instance** 여부를 통해 생성할 지, 수정할지 결정
    - 제공되지 않을 경우 save()는 지정된 새 인스턴스를 만듦(CREATE)
    - 제공되면 save()는 해당 인스턴스를 수정
    
    ```python
    # CREATE
    form = ArticleForm(request.POST)
    form.save()
    
    # UPDATE()
    form = ArticleForm(request.POST, instance=article)
    	form.save()
    ```
    

### 2.5 UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체를 지정
1. **request.POST**
    - 사용자가 form을 통해 전송한 데이터(새로운데이터)
2. instance
    - 수정이 되는 대상
- views.py
    
    ```python
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        **form = ArticleForm(instance=article)**
        context = {
            'article': article,
            **'form' : form**
        }
        return render(request, 'articles/edit.html', context)
    ```
    
- template
    
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>EDIT</h1>
      <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        
      </form>
      <hr>
      <a href="{% url 'articles:detail' article.pk %}">뒤로가기</a>
    {% endblock content %}
    ```
    
- update - view 수정
    
    ```python
    # articles/views.py
    
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.Post, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    
        content = {
            'form':form,
            'article':article,
        }
        return ('articles:edit.html', context)
    ```
    

### 2.6 Form과 ModelForm

- 각자 역할이 다름
- **Form**
    - 사용자로부터 받은 데이터가 DB와 연관되어 있지 않은 경우에 사용
    - DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우
    - (예시- 로그인, 사용자의 데이터를 받아 인증과정에서만 사용{db 수정 없음})
- **ModelForm**
    - 사용자로부터 받은 데이터가 DB와 연관되어 있는 경우에 사용
    - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 알고 있기에 곧바로 save() 호출이 가능(?)

## - 3. Widgets 활용하기

### 위젯 작성 방법

1. **첫번째**
    
    ```python
    # articles/forms.py
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        
    
        class Meta:
            model = Article 
            fields = '__all__' 
            **widget= {
                '**title' : **forms.TextInput(attrs={
                    'class':'my-title',
                    'placeholder':'Enter the title', # 입력창 안내문구
                    'maxlength':10 # 위젯은 유효성 검사랑 관련 없음
                    }
                )
            }**
    ```
    
2. **두번째**
    
    ```python
    # articles/forms.py
    from django import forms
    from .models import Article
    
    **class ArticleForm(forms.ModelForm):
        title = forms.CharField(
            label='제목',
            widget=forms.TextInput(
                # 태그에 속성 넣기
                attrs={
                    'class':'my-title',
                    'placeholder':'Enter the title', # 입력창 안내문구
                    'maxlength':10 # 위젯은 유효성 검사랑 관련 없음
                }
            )
        )
    
        content = forms.CharField(
            label='내용',
            widget=forms.Textarea(
                attrs={
                    'class':'my-content',
                    'placeholder':'Enter the content', # 입력창 안내문구
                    'rows':5,
                    'cols':50,
                }
            ),
            error_messages={
                'required':'Please enter your content',
            }
        )**
    
        class Meta:
            model = Article 
            fields = '__all__' 
    
    ```
    
- 두번째 사용하기