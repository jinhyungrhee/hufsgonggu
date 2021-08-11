from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView
from django.views.generic.list import MultipleObjectMixin
from .models import Product, Review
from .forms import RegisterForm

class ProductList(ListView):
    model = Product
    template_name = 'goods/goodsList.html'

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'goods/goodsRegister.html'
    success_url = '../complete/'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

class ReviewList(ListView):
    model = Review
    template_name = 'review/reviewList.html'

class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'
    template_name = 'review/review-post.html'
    success_url = '../complete2/'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)