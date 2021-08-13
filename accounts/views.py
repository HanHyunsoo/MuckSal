from accounts.forms import LoginForm
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import auth

def signup(request):
    if request.method == "GET":
        return render(request,'registration/signup.html')
    elif request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        useremail = request.POST.get('useremail',None)

        res_data = {} #프론트에 던져줄 응답 데이터
        if not (username and password and re_password and useremail):
            res_data['error'] = "모든 값을 입력하세요"
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            #같으면 정보들로 인스턴스 생성
            user = User(
                username = username,
                password = make_password(password),
                useremail = useremail,
            )
            #저장
            user.save()
            auth.login(request,user)
        return render(request,'diet/create.html',res_data)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        #정상적인 데이터인지 확인
        if form.is_valid(): #forms.py에 정의한 clean 메소드 대로 검사
            request.session['user'] = form.user_id #로그인 session 추가 후 매칭된 user 모델의 pk를 세션.user로 추가
            return redirect('diet:create')
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})


def logout(request):
    if request.session['user']:
        del(request.session['user'])
    return redirect('/')

def index(request):
    return render(request,'registration/index.html')