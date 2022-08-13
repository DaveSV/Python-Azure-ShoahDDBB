
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from shoahDDBB.models import Movies

def index(request):
    response = render(request, "index.html")  # django.http.HttpResponse
    response.set_cookie(key='shoah', value=1939)
    return response

class catalog(ListView):
    model = Movies

def book(request):
    return render(request, 'shoahDDBB/book.html')

def author(request):
    return render(request, 'shoahDDBB/author.html')

def user(request):
    return render(request, 'shoahDDBB/user.html')

def search(request):
    return render(request, 'shoahDDBB/search.html')