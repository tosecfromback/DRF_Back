from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, ValidationError
# from .models import 
# from .forms import
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


### Index

### Post
class PostList(View):
    def get(self, request):
        context = {
            'title' : 'GPTQnAPost'
        }
        
        return render(request, 'post/post_list.html', context)
    def post(self, request):
        pass


### Comment
class CommentWrite(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class CommentDelete(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class CommentUpdate(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

### Reply
class ReplyWrite(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class ReplyDelete(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class ReplyUpdate(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

