from django.contrib import admin
from django.urls import path

def DesdeDepartamento(self):
    print('======Desde departamento=========')

urlpatterns = [
    path('departamento/', DesdeDepartamento),
]