"""HGG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import *
from APIs.views import ProductCreate, ProductList

urlpatterns = [
    path('noticeBoard/', noticeBoard, name="noticeBoard"),
    path('noticePost/', noticePost, name="noticePost"),
    path('', index, name="index"),
    path('purchase/',purchase, name="purchase"),
    # 수정 : path('register/', register, name="register"),
    path('register/', ProductCreate.as_view(), name='register'),
    #상품리스트 보여주기
    path('productList',ProductList.as_view(), name='productList'),
    path('review/', review, name="review"),
    path('complete/',registerComplete, name="registerComplete"),
    path('loginIndex/', loginIndex, name="loginIndex"),
    path('userInformation/', userInformation, name="userInformation"),
    path('signup/', signup, name="signup"),
]
