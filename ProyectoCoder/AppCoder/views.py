from typing import List

from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.template import Template, Context, loader

#Para la prueba unitaria
import string
import random


#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView






# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

      return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):

      avatares = Avatar.objects.filter(user=request.user.id)
      
      return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


# BUSCAR OBJETOS
def buscarBoton(request):
      return render(request, "AppCoder/buscarBoton.html")


def buscar(request):
      
      if  request.GET["nombre"]:
            
            nombre = request.GET['nombre'] 
            tees = Tees.objects.filter(nombre__icontains=nombre)
            bottoms = Bottom.objects.filter(nombre__icontains=nombre)
            outwear = Outwear.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/inicio.html", {"tees":tees,"bottoms":bottoms,"outwear":outwear, "nombre":nombre})

      else: 

            respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      #return HttpResponse(respuesta)
      return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})

# def buscar(request):
      
#       if  request.GET["camada"]:
            
#             camada = request.GET['camada'] 
#             cursos = Curso.objects.filter(camada__icontains=camada)

#             return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

#       else: 

# 	      respuesta = "No enviaste datos"

#       #No olvidar from django.http import HttpResponse
#       #return HttpResponse(respuesta)
#       return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})



# LEER OBJETOS
def leerOutwear(request):
      datos = Outwear.objects.all()
      diccionario = {'outwears':datos}
      plantilla = loader.get_template('AppCoder/leerOutwears.html')
      documento_html = plantilla.render(diccionario)
      return HttpResponse(documento_html)

def leerBottoms(request):
      datos = Bottom.objects.all()
      diccionario = {'bottoms':datos}
      plantilla = loader.get_template('AppCoder/leerBottoms.html')
      documento_html = plantilla.render(diccionario)
      return HttpResponse(documento_html)


def leerTees(request):
      datos = Tees.objects.all()
      diccionario = {'tees':datos}
      plantilla = loader.get_template('AppCoder/leerTees.html')
      documento_html = plantilla.render(diccionario)
      return HttpResponse(documento_html)


def leerProfesor(request):
      datos = Profesor.objects.all()
      diccionario = {'profesores':datos}
      plantilla = loader.get_template('AppCoder/leerProfesor.html')
      documento_html = plantilla.render(diccionario)
      return HttpResponse(documento_html)

def leerCurso(request):
      datos = Curso.objects.all()
      diccionario = {'cursos':datos}
      plantilla = loader.get_template('AppCoder/leerCurso.html')
      documento_html = plantilla.render(diccionario)
      return HttpResponse(documento_html)


def leerEstudiante(request):
      datos = Estudiante.objects.all()
      diccionario = {'estudiantes':datos}
      plantilla = loader.get_template('AppCoder/leerEstudiante.html')
      documento_html = plantilla.render(diccionario)
      return HttpResponse(documento_html)



# AGREGAR OBJETOS
def agregarOutwears(request):

      if request.method == 'POST':

            miFormulario = formularioOutwear(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data

                  outwear = Outwear (nombre=informacion['nombre'], precio=informacion['precio'], imagen=informacion['imagen']) 

                  outwear.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
            
      else: 

            miFormulario= formularioOutwear() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarOutwears.html", {"miFormulario":miFormulario})
            

def agregarBottoms(request):

      if request.method == 'POST':

            miFormulario = formularioBottom(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data

                  bottom = Bottom (nombre=informacion['nombre'], precio=informacion['precio'], imagen=informacion['imagen']) 

                  bottom.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= formularioBottom() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarBottoms.html", {"miFormulario":miFormulario})


def agregarTees(request):

      if request.method == 'POST':

            miFormulario = formularioTees(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data

                  tee = Tees (nombre=informacion['nombre'], precio=informacion['precio'], imagen=informacion['imagen']) 

                  tee.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= formularioTees() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarTees.html", {"miFormulario":miFormulario})


def agregarCursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarCursos.html", {"miFormulario":miFormulario})



def agregarProfesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data
                  """
                  #CASO DE PRUEBA
                  KEY_LEN = 20
                  keylistNombre = [random.choice((string.ascii_letters + string.digits)) for i in range(KEY_LEN)]
                  nombrePrueba = "".join(keylistNombre)

                  print(f"---->Pueba con: {nombrePrueba} ")
                  """
                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarProfesor.html", {"miFormulario":miFormulario})


def agregarEstudiantes(request):
      if request.method == 'POST':

            miFormulario = EstudianteFormulario(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data

                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email']) 

                  estudiante.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= EstudianteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarEstudiantes.html", {"miFormulario":miFormulario})




# ELIMINAR/EDITAR OBJETOS

def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al men??
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesor.html",contexto)


def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aqu?? mellega toda la informaci??n del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})






















class CursoList(ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"




def logout_request(request):
      logout(request)
     
      return redirect("inicio")
     

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})



@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificar??n
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aqu?? mellega toda la informaci??n del html

            if miFormulario.is_valid:   #Si pas?? la validaci??n de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})


def urlImagen():

      return "/media/avatares/logo.png"