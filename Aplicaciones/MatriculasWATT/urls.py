from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('listaCarrera/', views.listaCarrera),
    path('listaCurso/', views.listaCurso),
    path('listaAsignatura/', views.listaAsignatura),
    path('crearCarrera/', views.crearCarrera),
    path('crearCurso/', views.crearCurso),
    path('crearAsignatura/', views.crearAsignatura),
    path('eliminarCarrera/<int:id>', views.eliminarCarrera),
    path('eliminarCurso/<int:id>', views.eliminarCurso),
    path('eliminarAsignatura/<int:id>', views.eliminarAsignatura),
    path('editarCarrera/<int:id>', views.editarCarrera),
    path('editarCurso/<int:id>', views.editarCurso),
    path('editarAsignatura/<int:id>', views.editarAsignatura),
    path('actualizarCarrera/<int:id>', views.actualizarCarrera),
    path('actualizarCurso/<int:id>', views.actualizarCurso),
    path('actualizarAsignatura/<int:id>', views.actualizarAsignatura),
]