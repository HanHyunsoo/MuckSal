from accounts.forms import LoginForm, ProfileForm,SignupForm
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile, User
from django.contrib.auth.hashers import make_password
from django.contrib import auth


def signup(request):
    if request.method =='POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.signup()
            return render(request,'diet/create.html')
    else:
        signup_form = SignupForm()
    
    context = {
        'signup_form' : signup_form
    }
    return render(request,'registration/signup.html',context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        #정상적인 데이터인지 확인
        if form.is_valid(): #forms.py에 정의한 clean 메소드 대로 검사
            # request.session['user'] = form.user_id #로그인 session 추가 후 매칭된 user 모델의 pk를 세션.user로 추가
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                auth.login(request, user)
                print(user)
            return redirect('diet:create')
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})


def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    return render(request,'registration/index.html')

def people(request):
    person = get_object_or_404(auth.get_user_model(), id=request.user.id)
    return render(request,'registration/people.html',{'person':person})

def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people')
        return redirect('registration/profile.html')
    else:
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'registration/profile.html', {
            'profile_form':profile_form
        })

def changePassword(request):
    if request.method == "POST":
        user_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if user_change_form.is_valid():
            user = user_change_form.save()
            return redirect('people')
        return redirect('registration/profile.html')
    else:
        user_change_form = PasswordChangeForm(user=request.user)
        return render(request, 'registration/changePassword.html', {
            'user_change_form':user_change_form
        })

