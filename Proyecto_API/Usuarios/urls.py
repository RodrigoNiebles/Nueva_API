from django.urls import path
from .views import Registro
urlpatterns = [
    path('registro/',Registro.as_view(), name='registro'),
    path('registro/<int:ID>',Registro.as_view(), name='registro_process')
]    