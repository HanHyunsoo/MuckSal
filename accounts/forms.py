from django import forms
from .models import User #DB와 데이터 비교위한 참조
from django.contrib.auth.hashers import check_password #페스워드 비교위한 참조

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디",
        error_messages={
            'required': "아이디를 입력하세요"
        })
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput,
        error_messages={
            'required' : "비밀번호를 입력하세요"
        })
    #유효성 검사하는 clean 메소드 오버라이드
    def clean(self):
        clean_data = super().clean()
        #비어있지 않은 데이터면
        username = clean_data.get('username')
        password = clean_data.get('password')

        #회원 일치 조회
        if username and password: #둘 다 값이 있으면
            user = User.objects.get(username=username)

            if not check_password(password,user.password): #비밀번호 일치 안하면
                self.add_error('password','비밀번호가 틀렸습니다.') #password 필드에 에러메세지 추가
            else: #일치하면
                self.user_id = user.id #현재 일치하는 user에 pk(즉 id)를 user_id 변수로 생성
