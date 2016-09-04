# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasaLegislativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_curto', models.CharField(max_length=50, unique=True)),
                ('esfera', models.CharField(choices=[('MUNICIPAL', 'Municipal'), ('ESTADUAL', 'Estadual'), ('FEDERAL', 'Federal')], max_length=10)),
                ('local', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChefeExecutivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('mandato_ano_inicio', models.IntegerField()),
                ('mandato_ano_fim', models.IntegerField()),
                ('casas_legislativas', models.ManyToManyField(to='quiz.CasaLegislativa')),
            ],
        ),
        migrations.CreateModel(
            name='Indexadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.CharField(max_length=120)),
                ('principal', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Parlamentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parlamentar', models.CharField(blank=True, max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('localidade', models.CharField(blank=True, max_length=100)),
                ('casa_legislativa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.CasaLegislativa')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=12)),
                ('numero', models.IntegerField()),
                ('cor', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Proposicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prop', models.CharField(blank=True, max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('ano', models.CharField(max_length=4)),
                ('ementa', models.TextField(blank=True)),
                ('descricao', models.TextField(blank=True)),
                ('indexacao', models.TextField(blank=True)),
                ('data_apresentacao', models.DateField(null=True)),
                ('situacao', models.TextField(blank=True)),
                ('autor_principal', models.TextField(blank=True)),
                ('autores', models.ManyToManyField(null=True, related_name='demais_autores', to='quiz.Parlamentar')),
                ('casa_legislativa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.CasaLegislativa')),
            ],
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vot', models.CharField(blank=True, max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('resultado', models.TextField(blank=True)),
                ('proposicao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Proposicao')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não'), ('ABSTENCAO', 'Abstenção'), ('OBSTRUCAO', 'Obstrução'), ('AUSENTE', 'Ausente')], max_length=10)),
                ('parlamentar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Parlamentar')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Votacao')),
            ],
        ),
        migrations.AddField(
            model_name='parlamentar',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Partido'),
        ),
        migrations.AddField(
            model_name='chefeexecutivo',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Partido'),
        ),
    ]