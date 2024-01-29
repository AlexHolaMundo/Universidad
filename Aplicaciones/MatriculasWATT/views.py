from django.shortcuts import render, redirect
from .models import carreraWATT, cursoWATT, asignaturaWATT
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'home.html')

def listaCarrera(request):
    carreraBdd=carreraWATT.objects.all()
    return render(request, 'listaCarrera.html', {
        'carreras': carreraBdd
    })

def listaCurso(request):
    cursoBdd=cursoWATT.objects.all()
    carreraBdd=carreraWATT.objects.all()
    return render(request, 'listaCurso.html', {
        'cursos': cursoBdd, 'carreras': carreraBdd
    })

def listaAsignatura(request):
    asignaturaBdd=asignaturaWATT.objects.all()
    cursoBdd=cursoWATT.objects.all()
    return render(request, 'listaAsignatura.html', {
        'asignaturas': asignaturaBdd, 'cursos': cursoBdd
    })



def crearCarrera(request):
    nombreCarreraWATT = request.POST['nombreCarreraWATT']
    logoCarreraWATT = request.FILES.get('logoCarreraWATT')
    directorCarreraWATT = request.POST['directorCarreraWATT']
    fechaCreacionCarreraWATT = request.POST['fechaCreacionCarreraWATT']
    descripcionCarreraWATT = request.POST['descripcionCarreraWATT']

    nuevaCarrera= carreraWATT.objects.create(
        nombreCarreraWATT=nombreCarreraWATT,
        logoCarreraWATT=logoCarreraWATT,
        directorCarreraWATT=directorCarreraWATT,
        fechaCreacionCarreraWATT=fechaCreacionCarreraWATT,
        descripcionCarreraWATT=descripcionCarreraWATT
    )
    messages.success(request, 'Carrera creada correctamente')
    return redirect('/listaCarrera')

def crearCurso(request):
    nivelCursoWATT = request.POST['nivelCursoWATT']
    descripcionCursoWATT = request.POST['descripcionCursoWATT']
    aulaCursoWATT = request.POST['aulaCursoWATT']
    horarioCursoWATT = request.FILES.get('horarioCursoWATT')

    carrera = request.POST['idCarreraWATT']
    carreraSeleccionada = carreraWATT.objects.get(idCarreraWATT=carrera)

    nuevoCurso= cursoWATT.objects.create(
        nivelCursoWATT=nivelCursoWATT,
        descripcionCursoWATT=descripcionCursoWATT,
        aulaCursoWATT=aulaCursoWATT,
        horarioCursoWATT=horarioCursoWATT,
        carrera=carreraSeleccionada
    )
    messages.success(request, 'Curso creado correctamente')
    return redirect('/listaCurso')

def crearAsignatura(request):
    nombreAsignaturaWATT = request.POST['nombreAsignaturaWATT']
    creditosAsignaturaWATT = request.POST['creditosAsignaturaWATT']
    fechaInicioAsignaturaWATT = request.POST['fechaInicioAsignaturaWATT']
    fechaFinalizacionAsignaturaWATT = request.POST['fechaFinalizacionAsignaturaWATT']
    profesorAsignaturaWATT = request.POST['profesorAsignaturaWATT']
    silaboAsignaturaWATT = request.FILES.get('silaboAsignaturaWATT')
    descripcionAsignaturaWATT = request.POST['descripcionAsignaturaWATT']
    departamentoAsignaturaWATT = request.POST['departamentoAsignaturaWATT']

    curso = request.POST['idCursoWATT']
    cursoSeleccionado = cursoWATT.objects.get(idCursoWATT=curso)

    nuevaAsignatura= asignaturaWATT.objects.create(
        nombreAsignaturaWATT=nombreAsignaturaWATT,
        creditosAsignaturaWATT=creditosAsignaturaWATT,
        fechaInicioAsignaturaWATT=fechaInicioAsignaturaWATT,
        fechaFinalizacionAsignaturaWATT=fechaFinalizacionAsignaturaWATT,
        profesorAsignaturaWATT=profesorAsignaturaWATT,
        silaboAsignaturaWATT=silaboAsignaturaWATT,
        descripcionAsignaturaWATT=descripcionAsignaturaWATT,
        departamentoAsignaturaWATT=departamentoAsignaturaWATT,
        curso=cursoSeleccionado
    )
    messages.success(request, 'Asignatura creada correctamente')
    return redirect('/listaAsignatura')


def eliminarCarrera(request, id):
    carreraEliminar=carreraWATT.objects.get(idCarreraWATT=id)
    carreraEliminar.delete()
    messages.success(request, 'Carrera eliminada correctamente')
    return redirect('/listaCarrera')

def eliminarCurso(request, id):
    cursoEliminar=cursoWATT.objects.get(idCursoWATT=id)
    cursoEliminar.delete()
    messages.success(request, 'Curso eliminado correctamente')
    return redirect('/listaCurso')

def eliminarAsignatura(request, id):
    asignaturaEliminar=asignaturaWATT.objects.get(idAsignaturaWATT=id)
    asignaturaEliminar.delete()
    messages.success(request, 'Asignatura eliminada correctamente')
    return redirect('/listaAsignatura')


def editarCarrera(request, id):
    carreraEditar=carreraWATT.objects.get(idCarreraWATT=id)
    return render(request, 'editCarrera.html', {
        'carrera': carreraEditar
    })

def editarCurso(request, id):
    cursoEditar=cursoWATT.objects.get(idCursoWATT=id)
    carreraBdd=carreraWATT.objects.all()
    return render(request, 'editCurso.html', {
        'curso': cursoEditar, 'carreras': carreraBdd
    })

def editarAsignatura(request, id):
    asignaturaEditar=asignaturaWATT.objects.get(idAsignaturaWATT=id)
    cursoBdd=cursoWATT.objects.all()
    return render(request, 'editAsignatura.html', {
        'asignatura': asignaturaEditar, 'cursos': cursoBdd
    })


def actualizarCarrera(request):
    id = request.POST['idCarreraWATT']
    nombreCarreraWATT = request.POST['nombreCarreraWATT']
    logoCarreraWATT = request.FILES.get('logoCarreraWATT')
    directorCarreraWATT = request.POST['directorCarreraWATT']
    fechaCreacionCarreraWATT = request.POST['fechaCreacionCarreraWATT']
    descripcionCarreraWATT = request.POST['descripcionCarreraWATT']

    carreraActualizar=carreraWATT(
        idCarreraWATT=id,
        nombreCarreraWATT=nombreCarreraWATT,
        logoCarreraWATT=logoCarreraWATT,
        directorCarreraWATT=directorCarreraWATT,
        fechaCreacionCarreraWATT=fechaCreacionCarreraWATT,
        descripcionCarreraWATT=descripcionCarreraWATT
    )
    carreraActualizar.save()
    messages.success(request, 'Carrera actualizada correctamente')
    return redirect('/listaCarrera')

def actualizarCurso(request):
    id = request.POST['idCursoWATT']
    nivelCursoWATT = request.POST['nivelCursoWATT']
    descripcionCursoWATT = request.POST['descripcionCursoWATT']
    aulaCursoWATT = request.POST['aulaCursoWATT']
    horarioCursoWATT = request.FILES.get('horarioCursoWATT')

    carrera = request.POST['idCarreraWATT']
    carreraSeleccionadaWATT = carreraWATT.objects.get(idCarreraWATT=carrera)

    cursoActualizar=cursoWATT(
        idCursoWATT=id,
        nivelCursoWATT=nivelCursoWATT,
        descripcionCursoWATT=descripcionCursoWATT,
        aulaCursoWATT=aulaCursoWATT,
        horarioCursoWATT=horarioCursoWATT,
        carrera=carreraSeleccionadaWATT
    )
    cursoActualizar.save()
    messages.success(request, 'Curso actualizado correctamente')
    return redirect('/listaCurso')

def actualizarAsignatura(request):
    id=request.POST['idAsignaturaWATT']
    nombreAsignaturaWATT = request.POST['nombreAsignaturaWATT']
    creditosAsignaturaWATT = request.POST['creditosAsignaturaWATT']
    fechaInicioAsignaturaWATT = request.POST['fechaInicioAsignaturaWATT']
    fechaFinalizacionAsignaturaWATT = request.POST['fechaFinalizacionAsignaturaWATT']
    profesorAsignaturaWATT = request.POST['profesorAsignaturaWATT']
    silaboAsignaturaWATT = request.FILES.get('silaboAsignaturaWATT')
    descripcionAsignaturaWATT = request.POST['descripcionAsignaturaWATT']
    departamentoAsignaturaWATT = request.POST['departamentoAsignaturaWATT']
    curso = request.POST['idCursoWATT']
    cursoSeleccionadoWATT = cursoWATT.objects.get(idCursoWATT=curso)

    asignaturaActualizar=asignaturaWATT(
        idAsignaturaWATT=id,
        nombreAsignaturaWATT=nombreAsignaturaWATT,
        creditosAsignaturaWATT=creditosAsignaturaWATT,
        fechaInicioAsignaturaWATT=fechaInicioAsignaturaWATT,
        fechaFinalizacionAsignaturaWATT=fechaFinalizacionAsignaturaWATT,
        profesorAsignaturaWATT=profesorAsignaturaWATT,
        silaboAsignaturaWATT=silaboAsignaturaWATT,
        descripcionAsignaturaWATT=descripcionAsignaturaWATT,
        departamentoAsignaturaWATT=departamentoAsignaturaWATT,
        curso=cursoSeleccionadoWATT
    )
    asignaturaActualizar.save()
    messages.success(request, 'Asignatura actualizada correctamente')
    return redirect('/listaAsignatura')

def enviar_correo(request):
    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        asunto = request.POST.get('asunto')
        cuerpo = request.POST.get('cuerpo')

        send_mail(asunto, cuerpo, settings.EMAIL_HOST_USER, [destinatario], fail_silently=False)

        messages.success(request, 'Correo enviado correctamente')
        return HttpResponseRedirect('/enviar_correo')
    return render(request, 'correo.html')