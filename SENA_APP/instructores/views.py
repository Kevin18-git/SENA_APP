from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Instructor
from .forms import InstructorForm

# Create your views here.

def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('apellido', 'nombre')
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    template = loader.get_template('detalle_instructor.html')
    
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    
    return HttpResponse(template.render(context, request))

def crear_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            try:
                instructor = form.save()
                messages.success(
                    request, 
                    f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.'
                )
                return redirect('instructores:lista_instructores') 
            except Exception as e:
                messages.error(request, f'Error al guardar el instructor: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
            print("Errores del formulario:", form.errors)
    else:
        form = InstructorForm()
    
    return render(request, 'crear_instructor.html', {
        'form': form,
        'titulo': 'Registrar Nuevo Instructor'
    })