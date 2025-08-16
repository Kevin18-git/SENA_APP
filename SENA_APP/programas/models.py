from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Programa")
    ficha = models.CharField(max_length=100, unique=True, verbose_name="Ficha del Programa")
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inicio")
    fecha_finalizacion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Finalización")
    
    NIVELES_FORMACION = [
        ('Tecnologo', 'Tecnólogo'),
        ('Tecnico', 'Técnico'),
        ('Especializacion', 'Especialización Tecnológica'),
    ]

    nivel_formacion = models.CharField(
        max_length=20,
        choices=NIVELES_FORMACION,
        default='Tecnologo',
        verbose_name='Nivel de Formación'
    )
    

    def __str__(self):
        return f"{self.nombre} - {self.ficha}"

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Programas"