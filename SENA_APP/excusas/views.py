from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Excusa
from .forms import ExcusaForm
from django.db.models import Q 

def crear_excusa(request):
    if request.method == 'POST':
        form = ExcusaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Excusa registrada exitosamente.")
            return redirect('excusas:crear_excusa')
    else:
        form = ExcusaForm()
    
    context = {'form': form, 'titulo': 'Registrar Excusa'}
    return render(request, 'crear_excusa.html', context) # <--- CORREGIDO

def lista_excusas(request):
    query = request.GET.get('q')
    tipo = request.GET.get('tipo')
    estado = request.GET.get('estado')

    excusas = Excusa.objects.all().order_by('-fecha_registro')

    if query:
        excusas = excusas.filter(
            Q(aprendiz__nombre__icontains=query) |
            Q(motivo__icontains=query)
        )
    if tipo:
        excusas = excusas.filter(tipo_excusa=tipo)

    if estado:
        excusas = excusas.filter(estado=estado)

    context = {
        'excusas': excusas,
        'total_excusas': excusas.count(),
        'titulo': 'Lista de Excusas',
        'query': query,
        'tipos_excusa': Excusa.TIPO_EXCUSA_CHOICES,
        'estados_excusa': Excusa.ESTADO_CHOICES,
        'tipo_seleccionado': tipo,
        'estado_seleccionado': estado,
    }
    return render(request, 'lista_excusas.html', context) # <--- CORREGIDO

def detalle_excusa(request, excusa_id):
    excusa = get_object_or_404(Excusa, id=excusa_id)
    return render(request, 'detalle_excusa.html', {'excusa': excusa}) # <--- CORREGIDO

def actualizar_estado_excusa(request, excusa_id):
    if request.method == 'POST':
        excusa = get_object_or_404(Excusa, id=excusa_id)
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(Excusa.ESTADO_CHOICES):
            excusa.estado = nuevo_estado
            excusa.save()
            messages.success(request, f"Estado de la excusa actualizado a '{nuevo_estado}'.")
    return redirect('excusas:lista_excusas')