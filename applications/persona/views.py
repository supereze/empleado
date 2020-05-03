from django.shortcuts import render
from django.views.generic import (
    ListView
)
#Models
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = "first_name"
    model = Empleado
    #http://127.0.0.1:8000/listar-todo-empleados/?page=1


class ListByArea(ListView):
    """Lista empleados de una area"""
    template_name = "persona/list_by_area.html" 

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista


class ListByJob(ListView):
    """Lista empleados de trabajo"""
    template_name = "persona/list_by_job.html" 

    def get_queryset(self):
        job = self.kwargs['job']
        lista = Empleado.objects.filter(
            job=job
        )
        return lista


class ListByKword(ListView):
    """Lista empleados por palabra clave"""
    template_name = "persona/list_by_kword.html" 
    context_object_name = 'empleados'
    def get_queryset(self):
        print('**************')
        #,""  porque es una tupla
        palabra_clave = self.request.GET.get("kword","")
        print("======", palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave 
        )
        print("lista resultado: ", lista    )
        return lista


class ListByHabilidades(ListView):
    """Lista de habilidades por empleado"""
    template_name = "persona/list_by_habilidades.html" 
    context_object_name = 'habilidades'
    def get_queryset(self):
        empleadoId = self.kwargs["empleadoId"]
        empleado = Empleado.objects.get(id=int(empleadoId))
        return empleado.habilidades.all()