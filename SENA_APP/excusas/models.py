from django.db import models
from aprendices.models import Aprendiz 
from programas.models import Programa 

class Excusa(models.Model):
    TIPO_EXCUSA_CHOICES = [
        ('Medica', 'Médica'),
        ('Laboral', 'Laboral'),
        ('Personal', 'Personal'),
        ('Otro', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Recibida', 'Recibida'),
        ('No Recibida', 'No Recibida'),
    ]

    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    tipo_excusa = models.CharField(max_length=50, choices=TIPO_EXCUSA_CHOICES)
    motivo = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Pendiente')
    archivo_adjunto = models.FileField(upload_to='excusas_adjuntos/', blank=True, null=True)

    def __str__(self):
        return f'Excusa de {self.aprendiz.nombre} - {self.tipo_excusa}'