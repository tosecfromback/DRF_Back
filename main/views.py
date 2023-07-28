from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
# from django.db import models
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request):
        context ={
            'title' : 'Main_Index',
        }

        return render(request, 'main/index.html', context)