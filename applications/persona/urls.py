from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('lista-by-area/<shortname>/', views.ListByArea.as_view()),
    path('lista-by-job/<job>/', views.ListByJob.as_view()),
    path('buscar-empleado/', views.ListByKword.as_view()),
    path('lista-by-habilidades/<empleadoId>/', views.ListByHabilidades.as_view()),
]