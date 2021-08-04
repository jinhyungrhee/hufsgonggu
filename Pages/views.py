from django.shortcuts import render

# Create your views here.
def noticeBoard(request):
    return render(request,'notice/notice-board.html')

def noticePost(request):
    return render(request, 'notice/notice-post.html')

def index(request):
    return render(request, 'main/index.html')

def purchase(request):
    return render(request, 'goods/purchase.html')

def register(request):
    return render(request, 'goods/goodsRegister.html')

def review(request):
    return render(request, 'review/review-post.html');

def registerComplete(request):
    return render(request, 'complete/register-complete.html')

def loginIndex(request):
    return render(request, 'login/login-main.html')