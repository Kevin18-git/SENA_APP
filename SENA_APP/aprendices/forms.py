
from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = '__all__'
        exclude = ['fecha_registro']

    def clean_documento_identidad(self):
        documento = self.cleaned_data.get('documento_identidad')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        if self.instance and self.instance.documento_identidad == documento:
            return documento

        if Aprendiz.objects.filter(documento_identidad=documento).exists():
            raise forms.ValidationError("El documento de identidad ya se encuentra registrado.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono