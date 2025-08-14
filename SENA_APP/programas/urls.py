from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.programas, name='lista_programas'),
    path('crear/', views.crear_programa, name='crear_programa'),
    path('detalle/<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
]