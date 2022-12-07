from django.shortcuts import render,redirect
from administración.models import Usuario
from administración.forms import FormUsuario
from onlines.views import index

# Create your views here.
def usuarioData(request):
   usuario = Usuario.objects.all()
   data = {'usuario': usuario}
   return render(request, 'usuarioData.html', data)

def agregarUsuario(request):
   form = FormUsuario()
   if request.method == 'POST' :
      form = FormUsuario(request.POST)
      if form.is_valid() :
         form.save()
      return redirect('/usuario')
   data = {'form' : form}
   return render(request, 'agregarUsuario.html', data)

def actualizarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    form = FormUsuario(instance=usuario)
    if request.method == 'POST' :
        form = FormUsuario(request.POST, instance=usuario)
        if form.is_valid() :
            form.save()
        return redirect('/usuario')
    data = {'form' : form}
    return render(request, 'agregarUsuario.html', data)

def eliminarUsuario(request, id):
   usuario = Usuario.objects.get(id = id)
   usuario.delete()
   return redirect('/usuario')

def login(request):
   form = FormUsuario()
   if request.method == 'POST' :
      form = FormUsuario(request.POST)
      if form.is_valid() :
         usuario = form.cleaned_data['tipo_usuario']
         if usuario == 'Cliente':
            return redirect('/respuestaData')
         elif usuario == 'Abogado':
            return redirect('/preguntaData')
         else:
            return redirect('/usuario')
      else:
         form = FormUsuario()            
   data = {'form' : form}
   return render(request, 'loginUsuario.html', data)

