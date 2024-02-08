from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('actualizarCarrera/', views.actualizarCarrera),
    path('actualizarCurso/', views.actualizarCurso),
    path('actualizarAsignatura/', views.actualizarAsignatura),

    path('enviar_correo/', views.enviar_correo),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)