from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'ficha', 'fecha_finalizacion', 'nivel_formacion']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ficha': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_finalizacion': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-control'}),
        }