# Generated by Django 4.2.6 on 2024-01-27 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carreraWATT',
            fields=[
                ('idCarreraWATT', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCarreraWATT', models.CharField(max_length=50)),
                ('logoCarreraWATT', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('directorCarreraWATT', models.CharField(max_length=50)),
                ('fechaCreacionCarreraWATT', models.DateField()),
                ('descripcionCarreraWATT', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cursoWATT',
            fields=[
                ('idCursoWATT', models.AutoField(primary_key=True, serialize=False)),
                ('nivelCursoWATT', models.CharField(max_length=50)),
                ('descripcionCursoWATT', models.CharField(max_length=50)),
                ('aulaCursoWATT', models.CharField(max_length=50)),
                ('horarioCursoWATT', models.FileField(blank=True, null=True, upload_to='horarios')),
                ('carreraWATT', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='MatriculasWATT.carrerawatt')),
            ],
        ),
        migrations.CreateModel(
            name='asignaturaWATT',
            fields=[
                ('idAsignaturaWATT', models.AutoField(primary_key=True, serialize=False)),
                ('nombreAsignaturaWATT', models.CharField(max_length=50)),
                ('creditosAsignaturaWATT', models.IntegerField()),
                ('fechaInicioAsignaturaWATT', models.DateField()),
                ('fechaFinalizacionAsignaturaWATT', models.DateField()),
                ('profesorAsignaturaWATT', models.CharField(max_length=50)),
                ('silaboAsignaturaWATT', models.FileField(blank=True, null=True, upload_to='silabos')),
                ('descripcionAsignaturaWATT', models.CharField(max_length=50)),
                ('departamentoAsignaturaWATT', models.CharField(max_length=50)),
                ('cursoWATT', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='MatriculasWATT.cursowatt')),
            ],
        ),
    ]
