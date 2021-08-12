from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from .models import Product, Review
from .forms import RegisterForm, UserForm
from .models import Product, Review, Apply
from .forms import RegisterForm

class ProductList(ListView):
    model = Product
    template_name = 'goods/goodsList.html'

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'goods/goodsRegister.html'
    success_url = '../complete1/'

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

def signup(request):
    # 계정 생성
    if request.method == "POST":
        
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)

            login(request, user) #로그인
            return redirect('/')

    else:
        form = UserForm()
    return render(request, 'signup/signup.html')
class GoodsDetail(DetailView):
    model = Product # queryset = Product.objects.all()과 동일
    template_name = 'goods/goodsDetail.html'
    context_object_name = "product"

    # pk 가져오기
    def get_context_data(self, **kwargs):
        #생성된 context는 Template으로 전달됨
        context = super().get_context_data(**kwargs)
        #context['prodcut_list'] = Product.objects.filter()
        return context

class ApplyCreate(CreateView):
    model = Apply
    fields = '__all__'
    template_name = 'goods/purchase.html'
    success_url = '../complete3/'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)
