from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Aprendiz, Curso
from .forms import AprendizForm
from instructores.models import Instructor
from programas.models import Programa
from excusas.models import Excusa


def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': lista_aprendices.count(),
    }
    return render(request, 'lista_aprendices.html', context)


def inicio(request):
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count()
    total_cursos = Curso.objects.count()
    cursos_activos = Curso.objects.filter(estado__in=['INI', 'EJE']).count()
    total_excusas = Excusa.objects.count()
    context = {
        'total_aprendices': total_aprendices,
        'total_cursos': total_cursos,
        'cursos_activos': cursos_activos,
        'total_instructores': total_instructores,
        'total_programas': total_programas,
        'total_excusas': total_excusas,
    }
    return render(request, 'inicio.html', context)


def lista_cursos(request):
    cursos = Curso.objects.all().order_by('-fecha_inicio')
    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
        'titulo': 'Lista de Cursos'
    }
    return render(request, 'cursos/lista_cursos.html', context)


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    return render(request, 'cursos/detalle_curso.html', context)


def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    context = {
        'aprendiz': aprendiz,
    }
    return render(request, 'aprendices/detalle_aprendiz.html', context)


class AprendizCreateView(generic.CreateView):
    model = Aprendiz
    form_class = AprendizForm
    template_name = "agregar_aprendiz.html"
    success_url = reverse_lazy('aprendices:lista_aprendices')

    def form_valid(self, form):
        messages.success(self.request, 'Aprendiz registrado exitosamente.')
        return super().form_valid(form)