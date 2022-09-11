from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.views.decorators.http import require_http_methods, require_safe, require_POST
# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
        'title':'게시글',
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method =='POST':
        article = ArticleForm(request.POST)
        if article.is_valid():
            article.save()
            return redirect('articles:index')
        else:
            print(f'에러 : {article.error}')
    else:
        article = ArticleForm()
    context = {
        'article':article,
        'title':'게시글 작성',
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article,
        'title':'글 세부내용',
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method=="POST":
        form= ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context={
        'article':article,
        'form':form,
        'title':" 글 수정"
    }
    return render(request, 'articles/update.html', context)

@require_POST
def delete(request, pk):
    if request.method=='POST':
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('articles:index')