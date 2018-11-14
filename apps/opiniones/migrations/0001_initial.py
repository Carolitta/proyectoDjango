# Generated by Django 2.1.2 on 2018-11-14 13:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Becario',
            fields=[
                ('id_becario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ap_pat', models.CharField(max_length=100)),
                ('ap_mat', models.CharField(blank=True, max_length=100, null=True)),
                ('generacion_proteco', models.CharField(choices=[('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37')], max_length=2)),
                ('correo', models.CharField(max_length=255, validators=[django.core.validators.EmailValidator(message='Email inválido')])),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('cupo', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)])),
                ('num_asistentes', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id_opinion', models.AutoField(primary_key=True, serialize=False)),
                ('calif_claridad', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('calif_material', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('calif_general', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('comentario', models.TextField()),
                ('becario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opiniones.Becario')),
                ('curso', models.ManyToManyField(to='opiniones.Curso')),
            ],
        ),
        migrations.AddField(
            model_name='becario',
            name='curso',
            field=models.ManyToManyField(to='opiniones.Curso'),
        ),
    ]