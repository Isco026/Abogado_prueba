from django.shortcuts import render,redirect
from onlines.models import Preguntas,Respuesta
from onlines.forms import FormPregunta,FormRespuesta


# Create your views here.
def index(request):
    return render(request, 'interfaz1.html')

def preguntaData(request):
   pregunta = Preguntas.objects.all()
   form = FormRespuesta()
   if request.method == 'POST' :
      form = FormRespuesta(request.POST)
      if form.is_valid() :
         form.save()
      return redirect('/preguntaData')
   data = {'pregunta': pregunta,'form' : form}
   return render(request, 'preguntaData.html', data)
   
def respuestaData(request):
   respuesta = Respuesta.objects.all()
   form = FormPregunta()
   if request.method == 'POST' :
      form = FormPregunta(request.POST)
      if form.is_valid() :
         form.save()
      return redirect('/respuestaData')
   data = {'respuesta': respuesta,'form' : form}
   return render(request, 'respuestaData.html', data)
