
from django.template.response import TemplateResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from shoahDDBB.models import Movies

def index(request):
    response = render(request, "index.html")  # django.http.HttpResponse
    response.set_cookie(key='shoah', value=1939)
    return response

class catalog(ListView):
    paginate_by = 10
    model = Movies

def movieDetail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    pk2 = pk +1
    context = {'movie': movie, 'pk2': pk2}
    return render(request, 'shoahDDBB/movieDetail.html', context)

def book(request):
    return render(request, 'shoahDDBB/book.html')

def author(request):
    return render(request, 'shoahDDBB/author.html')

def user(request):
    return render(request, 'shoahDDBB/user.html')

def search(request):
    return render(request, 'shoahDDBB/search.html')