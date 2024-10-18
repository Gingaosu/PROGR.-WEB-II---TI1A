from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/cargar-municipios/', views.cargar_municipios, name='ajax_cargar_municipios'),
]
