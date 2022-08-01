from django.urls import path
from . import views
from shoahDDBB.views import catalog
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog.as_view(), name='catalog'),
]