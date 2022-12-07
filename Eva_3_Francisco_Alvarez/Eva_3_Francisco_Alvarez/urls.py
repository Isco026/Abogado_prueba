"""Eva_3_Francisco_Alvarez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from onlines.views import index
from administración.views import usuarioData,login
from administración.views import agregarUsuario
from administración.views import actualizarUsuario
from administración.views import eliminarUsuario
from onlines.views import preguntaData,respuestaData 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', login),
    path('usuario/', usuarioData),
    path('agregarUsuario/', agregarUsuario),
    path('actualizarUsuario/<int:id>', actualizarUsuario),
    path('eliminarUsuario/<int:id>', eliminarUsuario),
    path('preguntaData/',preguntaData),
    path('respuestaData/',respuestaData)
]
