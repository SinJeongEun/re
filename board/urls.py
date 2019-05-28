"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',crud.views.layout, name='layout'),
    path('crud/home/', crud.views.home, name='home'),
    path('crud/new/', crud.views.new, name='new'),
    path('crud/create/', crud.views.create, name='create'),
    path('crud/newblog/', crud.views.blogform, name='newblog'),
    path('crud/<int:pk>/edit/', crud.views.edit, name = 'edit'),
    path('crud/<int:pk>/remove/', crud.views.remove, name = 'remove'),
    path('crud/<int:blog_id>/comment_create',crud.views.comment_create, name='comment_create'),
    path('crud/<int:blog_id>/comment_edit/<int:pk>/', crud.views.comment_edit, name = 'comment_edit'),
    path('crud/<int:blog_id>/comment_remove/<int:pk>/', crud.views.comment_remove, name= 'comment_remove'),
]

