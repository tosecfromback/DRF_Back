from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
# from .forms import SingupFrom, LoginForm

# Create your views here.

### UserMain
class Index(View):
    def get(self, request):
        context = {
            'title' : '로그인화면'
        }
        return render(request, 'account/index.html', context)
    def post(self, request):
        pass


### Signup


### Login
class Login(View):
    def get(self, request):
        context = {
            'title' : '로그인'
        }
        return render(request, 'login.html', context)
    def post(self, request):
        pass


### Logout


### 


###


###


###
