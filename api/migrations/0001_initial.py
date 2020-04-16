# Generated by Django 3.0.5 on 2020-04-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('salario', models.FloatField(verbose_name='Salario')),
                ('local', models.CharField(max_length=20, verbose_name='Local')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('contato', models.EmailField(max_length=254, verbose_name='Email')),
                ('tipo_contratacao', models.CharField(choices=[('CLT', 'Empregado registrado pela CLT'), ('TJ', 'Pessoa Jurídica')], max_length=3, verbose_name='Tipo de contratação')),
                ('tecnologias', models.ManyToManyField(to='api.Tecnologia')),
            ],
        ),
    ]