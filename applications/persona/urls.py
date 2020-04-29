from django.contrib import admin
from django.urls import path

def DesdePersona(self):
    print('======Desde persona=========')

urlpatterns = [
    path('persona/', DesdePersona),
]