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
from APIs.views import ProductCreate, ProductList, ReviewCreate, ReviewList, signup
from django.contrib.auth import views

from APIs.views import ProductCreate, ProductList, ReviewCreate, ReviewList, GoodsDetail, ApplyCreate

urlpatterns = [
    path('noticeBoard/', noticeBoard, name="noticeBoard"),
    path('noticePost/', noticePost, name="noticePost"),
    path('', index, name="index"),
    # 신청하기
    path('purchase/', ApplyCreate.as_view(), name="purchase"),
    # 수정 : path('register/', register, name="register"),
    path('register/', ProductCreate.as_view(), name='register'),
    # 상품리스트 보여주기
    path('productList/', ProductList.as_view(), name='productList'),
    path('review/', ReviewCreate.as_view(), name="review"),
    # 리뷰리스트 보여주기
    path('reviewList/', ReviewList.as_view(), name='reviewList'),
    # 상품등록 완료 페이지
    path('complete1/', registerComplete, name="registerComplete"),
    # 리뷰등록 완료 페이지
    path('complete2/', reviewComplete, name="reviewComplete"),
    path('login/', views.LoginView.as_view(template_name='login/login.html'), name="loginIndex"),
    # 신청 완료 페이지
    path('complete3/', applyComplete, name="applyComplete"),
    path('userInformation/', userInformation, name="userInformation"),
    path('signup/', signup, name="signup"),
    # 상품 상세보기
    path('goodsDetail/<int:pk>', GoodsDetail.as_view(), name="goodsDetail"),
    path('reviewBoard/', reviewBoard, name="reviewBoard"),
    path('submitComplete/',submitComplete,name="submitComplete"),
]
