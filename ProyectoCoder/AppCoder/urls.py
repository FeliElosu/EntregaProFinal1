from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView


from AppCoder import views
from .views import *




urlpatterns = [
   path('buscar/', views.buscar, name="buscar"),
   path('buscarBoton/', views.buscarBoton, name="buscarBoton"),
   
   # Ver Objetos
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('leerOutwears', views.leerOutwear, name="leerOutwears"),
    path('leerBottoms', views.leerBottoms, name="leerBottoms"),
    path('leerTees', views.leerTees, name="leerTees"),
    path('leerProfesor', views.leerProfesor, name="leerProfesor"),
    path('leerCurso', views.leerCurso, name="leerCurso"),
    path('leerEstudiante', views.leerEstudiante, name="leerEstudiante"),
    path('entregables', views.entregables, name="Entregables"),
    
    
    
    # Eliminar/Editar
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),

    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),



    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),

    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    # Agregar Objetos
    path('agregarOutwears', views.agregarOutwears, name="agregarOutwears"),
    path('agregarTees', views.agregarTees, name="agregarTees"),
    path('agregarBottoms', views.agregarBottoms, name="agregarBottoms"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('agregarProfesores', views.agregarProfesores, name="agregarProfesores"),
    path('agregarCursos', views.agregarCursos, name="agregarCursos"),
    path('agregarEstudiantes', views.agregarEstudiantes, name="agregarEstudiantes"),
    
]


