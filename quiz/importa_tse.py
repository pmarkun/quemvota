from django.db import transaction
from quiz import models
import csv, urllib.request, os

GENERO = 31
ID = 12
NOME = 15
PARTIDO = 19
PARTIDO_NUMERO = 18
PARTIDO_COR = "#000000"
EMAIL = 46

def baixa_foto(candid):
	url = "http://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/buscar/foto/2/"+str(candid)+'?x=1472871600000'
	nome = 'static/media/uploads/' + str(candid) + '.jpg'
	if not os.path.isfile('quiz/'+nome):
		foto = urllib.request.urlretrieve(url, 'quiz/'+nome)
	return nome

def rockandroll():
	transaction.set_autocommit(False)
	with open("quiz/dados/consulta_cand_2016_SP_capital.txt", 'r') as arquivo:
		candidatos = csv.reader(arquivo)
		next(candidatos)
		for c in candidatos:
			partido, _ = models.Partido.objects.get_or_create(nome=c[PARTIDO], defaults={ 'numero' : c[PARTIDO_NUMERO], 'cor' : PARTIDO_COR})
			defaultdict = {}
			defaultdict['foto'] = baixa_foto(c[ID])
			defaultdict['id_parlamentar'] = c[ID]
			defaultdict['genero'] = c[GENERO][0]	
			defaultdict['situacao'] = 'C'
			defaultdict['email'] = c[EMAIL]
			candidato, _ = models.Parlamentar.objects.get_or_create(nome=c[NOME], partido=partido, defaults=defaultdict)
			
		transaction.commit()