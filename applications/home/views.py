from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView
)
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/'


class HomeTemplate1View(TemplateView):
    template_name = 'home/home1.html'


class HomeTemplate2View(TemplateView):
    template_name = 'home/home2.html'


class HomeTemplate3View(TemplateView):
    template_name = 'home/home3.html'
    