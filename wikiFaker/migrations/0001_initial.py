# Generated by Django 4.1.7 on 2023-06-17 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='t1',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('posicion', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('foto', models.CharField(max_length=9999)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('correo', models.EmailField(max_length=200, unique=True)),
                ('contraseña', models.CharField(max_length=50, unique=True)),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='wikiFaker.genero')),
            ],
        ),
        migrations.CreateModel(
            name='puntos',
            fields=[
                ('id_punto', models.AutoField(db_column='idPunto', primary_key=True, serialize=False)),
                ('puntos', models.IntegerField(unique=True)),
                ('fecha_hora', models.CharField(max_length=100, unique=True)),
                ('id_usuario', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to='wikiFaker.usuario')),
            ],
        ),
    ]
