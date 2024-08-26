
from pdb import post_mortem
from webbrowser import get
from django.template.response import TemplateResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, request
from shoahDDBB.models import Movies
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    response = render(request, "index.html")  # django.http.HttpResponse
    response.set_cookie(key='shoah', value=1939)
    return response

class catalog(ListView):
    paginate_by = 5
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

def privacy(request):
    return render(request, 'shoahDDBB/privacy.html')

# @login_required
def support(request):
    return render(request, 'shoahDDBB/support.html')

def search_result(request):
    paginate_by = 5
    text = request.POST.get('search')
    list = Movies.objects.filter(mov_name__contains=text)
    total = Movies.objects.filter(mov_name__contains=text).count()
    context = {"movies_list": list, "text": text, "total": total}
    
    return render(request, 'shoahDDBB/movies_search.html', context)

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("catalog")
    template_name = "registration/signup.html"
    