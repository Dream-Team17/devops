from http.client import responses

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

class MainView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World</h1>")