from django import forms
from administración.models import Usuario
from django.core import validators

Tipo_Usuario = [('Abogado','Abogado'), ('Cliente', 'Cliente'), ('Administrador', 'Administrador')]
class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'tipo_usuario': forms.Select(
                choices=Tipo_Usuario
            )
        }
    
