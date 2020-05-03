from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('lista-by-area/<shortname>/', views.ListByArea.as_view()),
    path('lista-by-job/<job>/', views.ListByJob.as_view()),
    path('buscar-empleado/', views.ListByKword.as_view()),
    path('lista-by-habilidades/<empleadoId>/', views.ListByHabilidades.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
]