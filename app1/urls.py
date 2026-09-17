from django.urls import path
from . import views

app_name="app1"

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
]