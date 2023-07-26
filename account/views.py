from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .froms import RegisterAccount, Login

# Create your views here.

### UserMain
class Index(View):
    def get(self, request):
        context = {
            'title' : '로그인준비'
        }
        
        return render(request, 'account/account_index.html', context)
    def post(self, request):
        pass


### Signup
class Signup(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### Login
class Login(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

### Logout
class Logout(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### Profile
class ProfileDetail(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class ProfileUpdate(View):
    def get(self, requst):
        pass
    def post(self, request):
        pass


class UserSignout(View):
    def get(self, request):
        pass
    def post(self, request):
        pass