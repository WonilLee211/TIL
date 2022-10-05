from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (require_http_methods, require_POST,
                                          require_safe)

from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    # print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해달 게시글이 가진 모든 댓글 반환
    comments = article.comment_set.all()
    # article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
    # article = get_object_or_404(Article, pk=pk)
    # if request.method == 'POST':
    #     article.delete()
    #     return redirect('articles:index')
    # return redirect('articles:detail', article.pk)

# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:
#         if request.user == article.user:
#             article.delete()
#             return redirect('articles:index')
#         # 고객이 인증 상태와 비권한 상태로 삭제 요청시 403 반환
#         return HttpResponseForbidden()
#     # 고객이 비인증 상태로 삭제 요청 시, 401페이지 반환
#     return HttpResponse(status=401)
    

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            # Create a form to edit an existing Article,
            # but use POST data to populate the form.
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            # Creating a form to change an existing article.
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def comments_create(request, pk):
    # 로그인한 유저만 접근 허용
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        # modelform에서 제외시켰기 때문에 입력안해도 통과
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # 저장은 당장 하지않고 저장하고 나올 객체를 미리 준다.
            # 현재 요청하려는 문서에 요청한 유저 정보 넣기
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('accounts"login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)