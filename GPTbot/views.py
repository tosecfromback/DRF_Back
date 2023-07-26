from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse, reverse_lazy

class Index(View):
    def get(self, request):
        context = {
            'title' : 'Index',
        }
        return render(request, 'index.html', context)