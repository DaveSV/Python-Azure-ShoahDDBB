from django.urls import path
from . import views
from shoahDDBB.views import catalog, book
from django.views.generic import TemplateView
from .views import signup

urlpatterns = [
    path('', views.catalog.as_view(), name='catalog'),
    path('catalog/', views.catalog.as_view(), name='catalog'),
    path('search_result/', views.search_result, name='search_result'),
    path('book/', views.book, name='book'),
    path('user/', views.user, name='user'),
    path('search/', views.search, name='search'),
    path('author/', views.author, name='author'),
    path('support/', views.support, name='support'),
    path('privacy/', views.privacy, name='privacy'),
    path('catalog/<int:pk>', views.movieDetail, name='movieDetail'),
    path('signup/', signup.as_view(), name="signup"),
]