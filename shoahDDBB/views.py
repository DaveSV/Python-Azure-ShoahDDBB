
from pdb import post_mortem
from webbrowser import get
from django.template.response import TemplateResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, request
from shoahDDBB.models import Movies

def index(request):
    response = render(request, "index.html")  # django.http.HttpResponse
    response.set_cookie(key='shoah', value=1939)
    return response

class catalog(ListView):
    paginate_by = 10
    model = Movies
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(catalog, self).get_context_data(**kwargs)
        context['total'] = Movies.objects.count()
        return context
    

def movieDetail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    pk2 = pk +1
    movies_count = Movies.objects.count()
    if movies_count < pk2:
        pk2 = 1
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

def support(request):
    return render(request, 'shoahDDBB/support.html')

def search_result(request):
    paginate_by = 10
    text = request.POST.get('search')
    #text = "Holocaust"
    list = Movies.objects.filter(mov_name__contains=text)
    total = Movies.objects.filter(mov_name__contains=text).count()
    res = {"movies_list": list, "text": text, "total": total}
    
    return render(request, 'shoahDDBB/movies_search.html', res)