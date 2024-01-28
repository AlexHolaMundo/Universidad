from django.db import models

# Create your models here.
class carreraWATT(models.Model):
    idCarreraWATT = models.AutoField(primary_key=True)
    nombreCarreraWATT = models.CharField(max_length=50)
    logoCarreraWATT = models.FileField(upload_to='logos',null=True, blank=True)
    directorCarreraWATT = models.CharField(max_length=50)
    fechaCreacionCarreraWATT = models.DateField()
    descripcionCarreraWATT = models.CharField(max_length=50)
    def __str__(self):
        fila = "{0} {1} {2} {3} {4} {5}"
        return fila.format(self.idCarreraWATT, self.nombreCarreraWATT, self.logoCarreraWATT, self.directorCarreraWATT, self.descripcionCarreraWATT, self.fechaCreacionCarreraWATT)

class cursoWATT(models.Model):
    idCursoWATT = models.AutoField(primary_key=True)
    nivelCursoWATT = models.CharField(max_length=50)
    descripcionCursoWATT = models.CharField(max_length=50)
    aulaCursoWATT = models.CharField(max_length=50)
    horarioCursoWATT = models.FileField(upload_to='horarios',null=True, blank=True)
    carrera = models.ForeignKey(carreraWATT, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila = "{0} {1} {2} {3} {4} {5}"
        return fila.format(self.idCursoWATT, self.nivelCursoWATT, self.descripcionCursoWATT, self.aulaCursoWATT, self.horarioCursoWATT, self.carrera)

class asignaturaWATT(models.Model):
    idAsignaturaWATT = models.AutoField(primary_key=True)
    nombreAsignaturaWATT = models.CharField(max_length=50)
    creditosAsignaturaWATT = models.IntegerField()
    fechaInicioAsignaturaWATT = models.DateField()
    fechaFinalizacionAsignaturaWATT = models.DateField()
    profesorAsignaturaWATT = models.CharField(max_length=50)
    silaboAsignaturaWATT = models.FileField(upload_to='silabos',null=True, blank=True)
    descripcionAsignaturaWATT = models.CharField(max_length=50)
    departamentoAsignaturaWATT = models.CharField(max_length=50)
    curso= models.ForeignKey(cursoWATT, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} "
        return fila.format(self.idAsignaturaWATT, self.nombreAsignaturaWATT, self.creditosAsignaturaWATT, self.fechaInicioAsignaturaWATT, self.fechaFinalizacionAsignaturaWATT, self.profesorAsignaturaWATT, self.silaboAsignaturaWATT, self.descripcionAsignaturaWATT, self.departamentoAsignaturaWATT, self.curso)