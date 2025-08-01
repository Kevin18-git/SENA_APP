from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.lista_programas_view, name='lista_programas')
]