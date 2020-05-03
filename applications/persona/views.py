from django.shortcuts import render
from django.views.generic import (
    ListView
)
#Models
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    model = Empleado


class ListByAreaEmpleado(ListView):
    """Lista empleados de una area"""
    template_name = "persona/list_by_area.html" 

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista