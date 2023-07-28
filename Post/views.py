from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
# from django.contrib.auth.decorators import login_required

# Create your views here.


### PostList
class PostList(View):
    def get(self, request):
        context = {
            'title' : '질의응답 결과'
        }
        return render(request, 'post/post_index.html', context)
    def post(self, request):
        pass

### PostDetail
class PostDetail(View):
    def get(self, request):
        context = {
            'title' : '질의응답 상세페이지'
        }
        return render(request, 'post/post_detail.html', context)
    def post(self, request):
        pass

### PostSearch
class PostSearch(View):
    def get(self, request):
        context = {
            'title' : '질의응답 검색결과'
        }
        return render(request, 'post/post_search.html', context)
    def post(self, request):
        pass