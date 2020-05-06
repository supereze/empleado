from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#Models
from .models import Empleado


class InicioView(TemplateView):
    """ vista que carga la página de inicio """
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = "first_name"
    #model = Empleado
    #http://127.0.0.1:8000/listar-todo-empleados/?page=1
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave 
        )
        return lista


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


class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_persona.html"
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = [
        'first_name', 
        'last_name', 
        'job',
        'departamento',
        'habilidades',
    ]
    #fields = ("__all__")
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self,form):
        #logica del proceso
        #empleado = form.save() guarda en base de datos
        empleado = form.save(commit=False)#guarda en un instancia pero no en la base de datos
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name', 
        'last_name', 
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')
    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        #Aqui no se han validado los datos
        print('***************Method Post**********************')
        print('************************************************')
        print(request.POST)
        print(request.POST["last_name"])
        return super().post(request, *args, **kwargs)
    def form_valid(self,form):
        print('***************Method form valid****************')
        print('************************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:correcto')
