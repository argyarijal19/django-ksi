from django.urls import path, re_path
from . import views

app_name = 'myApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('postingan/', views.postingan, name='postingan')
]
