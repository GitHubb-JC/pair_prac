from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import review

# Create your views here.

def index(request):
    re = review.objects.all()
    context = {
        "re": re,
    }
    return render(request, 'movie_crud/index.html', context)

def new(request):
    return render(request, 'movie_crud/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    review.objects.create(title=title, content=content)
    return redirect('movie_crud:index')

def delete(request, re_pk):
    re = review.objects.get(pk=re_pk)
    re.delete()
    return redirect('movie_crud:index')

def detail(request, re_pk):
    re = review.objects.get(pk=re_pk)
    context = {
        're': re,
    }
    return render(request, 'movie_crud/detail.html', context)

def edit(request, re_pk):
    re = review.objects.get(pk=re_pk)
    context = {
        're': re
    }
    return render(request, 'movie_crud/edit.html', context)

def recreate(request, re_pk):
    re = review.objects.get(pk=re_pk)
    re.title = request.GET.get('title')
    re.content = request.GET.get('content')
    re.save()
    return redirect('movie_crud:index')
