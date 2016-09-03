from django.db import models

# Create your models here.
class Politico(models.Model):
	nome = models.CharField(max_length=200)
	partido = models.CharField(max_length=200)

class Votacao(models.Model):
	ementa = models.CharField(max_length=200)

class Voto(models.Model):
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    politico = models.ForeignKey(Politico, on_delete=models.CASCADE)
    voto = models.IntegerField(default=0)

