from django.contrib import admin
from .models import User,Profile

# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    # pass 이거 사용하면 상속만 받아서 새로운 클래스 생성
    list_display = ('username','password','useremail')

admin.site.register(User,AccountsAdmin)
admin.site.register(Profile)