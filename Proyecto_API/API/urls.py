from django.urls import path
from .views import PelisView
urlpatterns = [
    path('peliculas/',PelisView.as_view(), name='peliculas_list'),
    path('peliculas/<int:ID>',PelisView.as_view(), name='peliculas_process')
]
