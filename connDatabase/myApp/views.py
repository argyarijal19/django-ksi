from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Post

from .forms import PostForm
from .models import Post


def list(request):
    posts = Post.objects.all()

    context = {
        'page_title': 'Semua Post',
        'posts': posts,
    }

    return render(request, 'list.html', context)


def create(request):
    post_form = PostForm(request.POST or None)

    if request.method == 'POST':  # POST request dari browser
        if post_form.is_valid():
            post_form.save()

            return redirect('myApp:list')

    context = {
        'page_title': 'Create Post',
        'post_form': post_form,
    }

    return render(request, 'create.html', context)


def index(request):
    return render(request, 'home.html')


def postingan(request):
    db = Post.objects.all()
    context = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'postingan',
        'post': db
    }

    return render(request, 'index.html', context)
