# Generated by Django 4.2.6 on 2024-01-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatriculasWATT', '0005_alter_asignaturawatt_curso_alter_cursowatt_carrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrerawatt',
            name='logoCarreraWATT',
            field=models.FileField(blank=True, null=True, upload_to='logos'),
        ),
    ]
