from django.contrib import admin
from .models import carreraWATT, cursoWATT, asignaturaWATT
# Register your models here.
#admin.site.register(carreraWATT)
#admin.site.register(cursoWATT)
#admin.site.register(asignaturaWATT)

@admin.register(carreraWATT)
class carreraWATTAdmin(admin.ModelAdmin):
    list_display = ('nombreCarreraWATT', 'logoCarreraWATT', 'directorCarreraWATT', 'fechaCreacionCarreraWATT', 'descripcionCarreraWATT')
    search_fields = ('nombreCarreraWATT', 'descripcionCarreraWATT')
    list_editable = ( 'fechaCreacionCarreraWATT','directorCarreraWATT', 'descripcionCarreraWATT')
    list_display_links =('nombreCarreraWATT', 'logoCarreraWATT')
    list_filter = ('fechaCreacionCarreraWATT',)
    list_per_page = 3
    exclude = ('idCarreraWATT',)

@admin.register(cursoWATT)
class cursoWATTAdmin(admin.ModelAdmin):
    list_display = ( 'nivelCursoWATT', 'descripcionCursoWATT', 'aulaCursoWATT', 'horarioCursoWATT', 'carrera')
    search_fields = ('nivelCursoWATT', 'descripcionCursoWATT')
    list_filter = ('aulaCursoWATT',)
    list_editable = ('horarioCursoWATT', )
    list_per_page = 3
    exclude = ('idCursoWATT',)

@admin.register(asignaturaWATT)
class asignaturaWATTAdmin(admin.ModelAdmin):
    list_display = ('nombreAsignaturaWATT', 'descripcionAsignaturaWATT', 'creditosAsignaturaWATT', 'fechaInicioAsignaturaWATT', 'fechaFinalizacionAsignaturaWATT', 'profesorAsignaturaWATT', 'silaboAsignaturaWATT', 'departamentoAsignaturaWATT')
    search_fields = ('nombreAsignaturaWATT', 'descripcionAsignaturaWATT', 'departamentoAsignaturaWATT')
    list_display_links = ('nombreAsignaturaWATT',)
    list_editable=('descripcionAsignaturaWATT', 'creditosAsignaturaWATT')
    list_filter = ('profesorAsignaturaWATT',)
    list_per_page = 3
    exclude = ('idAsignaturaWATT',)