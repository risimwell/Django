# Generated by Django 4.1.2 on 2022-11-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=60)),
                ('cedula', models.TextField()),
                ('clave', models.TextField()),
                ('telefono', models.IntegerField()),
                ('fechaDeNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('fotoPerfil', models.ImageField(blank=True, null=True, upload_to='ApiPersonal\\Imagenes')),
                ('comoNosContacto', models.TextField()),
                ('numeroDeHijos', models.IntegerField()),
            ],
        ),
    ]
