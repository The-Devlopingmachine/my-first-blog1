from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('posts/new', views.post_new, name = 'new_post'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail')
]