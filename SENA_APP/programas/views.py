from django.shortcuts import render
from .models import Programa

def lista_programas_view(request):
    programas = Programa.objects.all().order_by('nombre')
    
    context = {
        'programas': programas,
        'total_programas': programas.count(),
    }
    
    # Cambia la ruta para que busque directamente en la carpeta 'templates'
    return render(request, 'lista_programas.html', context)