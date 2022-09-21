# 일반폼으로 입력받은 정보를 DB에 저장

- **일반폼으로 클라이언트 정보를 받아서 model 클래스로 저장하기**
1. 일반 폼 선언
    
    ```python
    # chattings/forms.py
    
    from django import forms
    
    class ChatForm(forms.Form):
        user = forms.CharField(max_length=10)
        content = forms.charField(widget=forms.Textarea())
    ```
    
    - 일반폼은 db에 관여하지 못한다.
2. 모델 클래스를 이용해서 저장하기 `models.py`
    
    ```python
    # chattings/forms.py
    
    from django.db import models
    
    class Chat(models.Model):
        user = models.CharField(max_length=10)
        content = models.TextField()
        create_at = DateTimeField(auto_now_add=True)
        update_at = DateTimeField(auto_now=True)
    ```
    
3. urls.py
    
    ```python
    from django.urls import path
    from . import views
    
    app_name='chattings'
    urlspatterns = [
        path('create/', views.create, name='create'),
    ]
    ```
    
4. views.py
    
    ```python
    from django.shortcuts import render
    from .forms import ChatForm
    from .models import Chat
    
    def Create(request):
        if request.method=="POST":
            form = CharForm(request.POST)
            if form.is_valid():
                chat = Chat()
                chat.user = form.cleaned_data['user']
                chat.content = form.cleaned_data['content']
                chat.save()
                return redirect('chattings:index')
        else:
            form = form()
        content = {
            'form':form
        }
        return render(request, 'chattings/create.html', context)
    
    ```