# SENA_APP/programas/models.py
from django.db import models

class Programa(models.Model):
    # Usar snake_case para nombres de campos
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Programa")
    ficha = models.CharField(max_length=100, unique=True, verbose_name="Ficha del Programa")
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inicio")
    fecha_finalizacion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Finalización")

    def __str__(self):
        return f"{self.nombre} - {self.ficha}"

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Programas"