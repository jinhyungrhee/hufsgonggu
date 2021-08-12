from django import forms
from django.forms import fields
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form 일단 사용X
# 일단은 formView대신 CreateView 사용해서 상품입력 완성했음

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        # 일단 'created_at'은 제외
        fields = ['name', 'price', 'description']

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(max_length=256, label="닉네임")
    kakaoId = forms.CharField(max_length=256, label="카카오톡 ID")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "nickname", "kakaoId"]