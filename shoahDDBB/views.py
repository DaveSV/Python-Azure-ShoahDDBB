
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views.generic import ListView

from shoahDDBB.models import Movies

def index(request):
    response = render(request, "index.html")  # django.http.HttpResponse
    response.set_cookie(key='shoah', value=1939)
    return response

class catalog(ListView):
    model = Movies
    