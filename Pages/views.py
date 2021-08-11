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
# review 테스트중
def review(request):
    return render(request, 'review/review-post.html');

# 상품등록완료
def registerComplete(request):
    return render(request, 'complete/register-complete.html')

# 리뷰등록완료
def reviewComplete(request):
    return render(request, 'complete/review-complete.html')

def loginIndex(request):
    return render(request, 'login/login-main.html')

def userInformation(request):
    return render(request, 'login/input-user-information.html')

def signup(request):
    return render(request, 'signup/signup.html')

def goodsDetail(request):
    return render(request, 'goods/goodsDetail.html')

def reviewBoard(request):
    return render(request, 'review/review-board.html')

def submitComplete(request):
    return render(request, 'complete/submit-complete.html')