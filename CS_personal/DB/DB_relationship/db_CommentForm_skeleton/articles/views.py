from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
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
    article = get_object_or_404(Article, pk=pk)
    
    # 댓글  목록 보여주기
    # DB에서 댓글 정보 가져오기
    # Comment.objects.all() 다른 글의 댓글도 들어옴
    # Comment.objects.get(pk=pk) 글의 댓글 하나만 조회됨
    comments = Comment.objects.filter(article=article) # 가능함!
    
    # 댓글 작성을 위한 입력폼
    # 반드시 html에서 사용할 수 있도록 전달해야 함
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.author:
            article.delete()
        return redirect('articles:detail', article.pk)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if not request.user == article.author:
        return redirect('articles:detail', article.pk)
        
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
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def comment_create(request, article_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if not request.user == article.author:
        return redirect('articles:detail', Article.objects.get(pk=article_pk))
    
    comment_form = CommentForm(request.POST)
    # 댓글 데이터를 넣기 위해 글 정보를 가져와야 함
    article = Article.objects.get(pk = article_pk)
    if comment_form.is_valid():
        # 그냥 저장하면  not null constraint failed
        comment=comment_form.save(commit=False) # commit : db에 저장되기 전에 사용자가 입력한 데이터의 인스턴스
        comment.article = article               # 글 정보 직접 입력
        comment.author = request.user
        comment.save()
        return redirect('articles:detail', article_pk)
    # 유효성검사를 통과하지 못하면
    # 리다이렉트를 하게 되면 에러정보를 전달하지 못함
    # 그래서 직접 렌더해야 함
    comments = article.comment_set.all()
    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments
    }
    return render(request, 'articles/detail.html', context)
    
@require_POST
def comment_delete(request, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(pk=comment_pk)
    article = comment.article
    # 삭제 요청 유저와 댓글 작성자가 일치할 때 댓글 삭제
    if comment.author == request.user:
        comment.delete()
    
    return redirect('articles:detail', article.pk)