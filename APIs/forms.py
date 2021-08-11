from django import forms
from .models import Product

# form 일단 사용X
# 일단은 formView대신 CreateView 사용해서 상품입력 완성했음

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        # 일단 'created_at'은 제외
        fields = ['name', 'price', 'description']