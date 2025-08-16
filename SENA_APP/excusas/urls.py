from django.urls import path
from . import views

app_name = 'excusas'

urlpatterns = [
    path('registrar/', views.crear_excusa, name='crear_excusa'),
    path('lista/', views.lista_excusas, name='lista_excusas'),
    path('detalle/<int:excusa_id>/', views.detalle_excusa, name='detalle_excusa'),
    path('actualizar_estado/<int:excusa_id>/', views.actualizar_estado_excusa, name='actualizar_estado'),
]