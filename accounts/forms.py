from django import forms
from .models import User,Profile #DB와 데이터 비교위한 참조
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

class ProfileForm(forms.models.ModelForm):
    nickname = forms.CharField(label="별명", required=False)
    description = forms.CharField(label="자기소개", required=False,widget=forms.Textarea())
    image = forms.ImageField(label="이미지",required=False)

    class Meta:
        model = Profile
        fields = ['nickname','description','image',]

class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form=control',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다.')
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다. 다시 확인해주세요')
        return password2
    
    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )