from django.shortcuts import render, redirect
from .models import Either, Comment
from .forms import EitherForm, CommentForm

# Create your views here.
def index(request):

    eithers = Either.objects.all()
    context = {
        'eithers':eithers,
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == "POST":
        form = EitherForm(request.POST)
        form.save()
        return redirect('eithers:index')

    form = EitherForm()
    context = {
        'form':form,
    }
    return render(request, 'eithers/create.html', context)

def detail(request, either_id):
    either = Either.objects.get(pk=either_id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(either=either)
    context = {
        'either':either,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'eithers/detail.html', context)


def create_comment(request, either_id):
    comment_form = CommentForm(request.POST)
    either = Either.objects.get(pk=either_id)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.either = either
        comment.save()
        return redirect("eithers:detail", either_id)    