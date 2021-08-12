from django import forms
from .models import Product, Review

# 일단 사용 X
# 일단은 formView대신 CreateView 사용해서 상품입력 완성했음

class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length=32, label="상품명"
    )
    price = forms.IntegerField(
        error_messages={'required': "상품가격을 입력하세요."},
        label="가격"
    )
    description = forms.CharField(
        error_messages={'required': "상품설명을 입력하세요."},
        label="상품설명"
    )
    image = forms.ImageField(
        error_messages={'required': "이미지를 등록하세요."},
        label="이미지"
    )
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        image = cleaned_data.get('image')

        if not(name and price and description and image):
            self.add_error('name', '값이 없습니다.')
            self.add_error('price', '값이 없습니다.')
            self.add_error('description', '값이 없습니다.')
            self.add_error('image', '값이 없습니다.')
