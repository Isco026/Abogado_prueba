from django import forms
from onlines.models import Preguntas,Respuesta
from django.core import validators

class FormPregunta(forms.ModelForm):
    class Meta:
        model = Preguntas
        fields = '__all__'

class FormRespuesta(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = '__all__'