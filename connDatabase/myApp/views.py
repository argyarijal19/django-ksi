from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post


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
