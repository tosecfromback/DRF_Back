from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, SigninForm

# Create your views here.

### UserMain
class Index(View):
    def get(self, request):
        context = {
            'title' : '사용자메인화면'
        }
        return render(request, 'account/index.html', context)
    def post(self, request):
        pass


### Signup
class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
             return redirect('main:index')
        form = SigninForm()
        context = {
            'form' : form, 
            'title' : '회원가입'
        }
    
        return render(request, 'account/signin.html', context)
    
    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('account:login')


### Login
class Login(View):
    def get(self, request):
        context = {
            'title' : '로그인'
        }
        return render(request, 'account/login.html', context)
    def post(self, request):
        pass


### Logout
class Logout(View):
    def get(self, request):
        context = {
            'title' : '로그아웃'
        }
        return render(request, 'account/logout.html', context)
    def post(self, request):
        pass


### Profile Detail
class Profile_Detail(View):
    def get(self, request):
        context = {
            'title' : '로그인'
        }
        return render(request, 'account/profile_detail.html', context)
    def post(self, request):
        pass

### Profile Update
class Profile_Update(View):
    def get(self, request):
        context = {
            'title' : '프로필 수정'
        }
        return render(request, 'account/profile_update.html', context)
    def post(self, request):
        pass


### Password Change
class PassChange(View):
    def get(self, request):
        context = {
            'title' : '비밀번호수정'
        }
        return render(request, 'account/password_chng.html', context)
    def post(self, request):
        pass


### User SignOut
class SignOut(View):
    def get(self, request):
        # context = {
        #     'title' : '회원탈퇴'
        # }
        # return render(request, 'account/login.html', context)
        pass
    def post(self, request):
        pass
