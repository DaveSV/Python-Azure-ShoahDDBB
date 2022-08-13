from django.urls import path
from . import views
from shoahDDBB.views import catalog, book
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog.as_view(), name='catalog'),
    path('book/', views.book, name='book'),
    path('user/', views.user, name='user'),
    path('search/', views.search, name='search'),
    path('author/', views.author, name='author'),
]