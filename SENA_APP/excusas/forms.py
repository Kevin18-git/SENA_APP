from django import forms
from .models import Excusa

class ExcusaForm(forms.ModelForm):
    class Meta:
        model = Excusa
        fields = ['aprendiz', 'programa', 'tipo_excusa', 'motivo', 'archivo_adjunto']
        widgets = {
            'aprendiz': forms.Select(attrs={'class': 'form-control'}),
            'programa': forms.Select(attrs={'class': 'form-control'}),
            'tipo_excusa': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'archivo_adjunto': forms.FileInput(attrs={'class': 'form-control'}),
        }