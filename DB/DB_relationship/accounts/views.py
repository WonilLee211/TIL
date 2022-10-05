from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm,  # UserCreationForm,
                                       PasswordChangeForm)
from django.shortcuts import redirect, render
from django.views.decorators.http import (  # require_http_methods(['GET',]); require_http_methods(['POST',])
    require_http_methods, require_POST, require_safe)

from .forms import CustomuserChangeForm, CustomUserCreationForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인한 사용자가 로그인 페이지를 볼 필요는 없음
    if request.user.is_authenticated:
        return redirect('articles:index')

    # 실제 로그인 동작이 일어날 때
    # session이 create되어 DB에 저장
    # POST요청일 때 로그인 동작을 처리해야 함
    if request.method == 'POST':
        # 사용자의 입력 데이터가 채워진 form을 생성
        # request.POST : 사용자의 모든 정보가 담겨 있음
        form = AuthenticationForm(request, request.POST)
        # 입력이 잘되었는지 그리고 회원인지 확인
        # 비밀번호가 잘못 적거나 회원가입이 안된 사람이 로그인 시도할 때 Fail
        if form.is_valid():
            # 우리 회원이라면 로그인 처리(session 생성해서 DB에 저장)
            # 유저 인스턴스가 필요한데 AuthenticationForm의 메소드 이용
                # form.get_user() : 유효성을 통과한 user instance 반환
            auth_login(request, form.get_user())
            # QueryString Paramter로 전달되는 데이터를 가져오는 방법
            # POST로 요청되었지만 GET은 QueryString Parameter로 전달된 주소를 받아오는 방법으로 사용됨
            next = request.GET.get('next')
            # next값이 있다면 next, 없다면 'articles:index'
            return redirect(next or 'articles:index')
            # 주의 : html에 action이 채워져있다면 실행이 안될 수도 있음
    else:
        form = AuthenticationForm()
    context = {
        # form.html 로 통합하기 위한 전달 데이터
        'form':form,
        'title':'로그인',
        'btn_title':'로그인'
    }
    return render(request, 'accounts/form.html', context)

@login_required
#@require_POST
def logout(request):
    # 로그아웃은 사용자로부터 입력받는 것이 없기에
    # GET 요청에 대한 처리는 필요 없다
    if request.method=="POST":
        # 로그아웃을 처리하는 내용
            # session을 DB에서 삭제
        auth_logout(request)

    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인 한 사용자는 회원가입 페이지를 접근할 필요가 없음
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # 1 회원가입 페이지 만들기
        form = CustomUserCreationForm()
    context = {
        'form':form,
        'title':'회원가입',
        'btn_title':'가입하기'
    }
    return render(request, 'accounts/form.html', context)

@login_required
#@require_POST
def delete(request):
    # 회원 탈퇴는 DB를 수정하느 것이기에 POST일 때만 동작
    if request.method=='POST':
        # user 정보는 request 내부에 가지고있어서
        # 따로  db에서 불러올 필요없음
        request.user.delete()
        auth_logout(request)
        # 회원 탈퇴하면 로그인 되어있을 때 필요가 없기 때문에 로그아웃
        # 탈퇴 전에 로그아웃을 하게 되면 request에 유저정보가 사라지기 때문에
        # 탈퇴 후에 로그아웃해야 한다.
        return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=='POST':
        # instance 값이 없으면 새로 생성하는 로직이 되어버럼
            # signup이랑 같은 형태가 된다.
        form = CustomuserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomuserChangeForm(instance=request.user)
    context = {
        'form':form,
        'title':'회원 정보 수정하기',
        'btn_title':'수정하기'
    }
    return render(request, 'accounts/form.html', context)

@login_required
def password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 일반 폼을 상속받았지만, save()함수가 정의되어 있음
            user = form.save()
            # 비밀번호가 변경되면 session의 유저데이터와 일치하지 않게 되는 현상 발생
            # session의 유저정보를 업데이트 시켜야 한다.
            # 인자 : request, 유저정보
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        # 로그인한 유저의 비밀번호를 저장해야 하기 때문에 
        # 첫번째 인자로 user 정보를 넣어야 한다.
        # 일반폼이라서 인스턴스형태로 넣지않고 바로 request.user를 인자로 넣는다.
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
        'title':'비밀번호 변경하기',
        'btn_title':'변경하기'
    }
    return render(request, 'accounts/form.html', context)
