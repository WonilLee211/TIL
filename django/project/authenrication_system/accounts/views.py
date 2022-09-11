from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.

def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
        'title':'login'
    }
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # return redirect('accounts:login')
            # 회원가입 후 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
        'title':'SIGNUP',
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    if request.method =="POST":
        auth_logout(request)
        return redirect('articles:index')

def delete(request):
    if request.method=="POST":
        request.user.delete()
        auth_logout(request)
        return redirect('articles:index')

def update(request):
    if request.method=="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
        'title':'회원정보수정'
    }
    return render(request, 'accounts/update.html', context)