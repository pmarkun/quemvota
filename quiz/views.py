from django.shortcuts import render, render_to_response
from django.template import RequestContext
from quiz.models import Proposicao, CasaLegislativa, Votacao

from .utils import MatrizesDeDadosBuilder
from .forms import CandidatoForm
from math import sqrt

# Create your views here.
from django.http import HttpResponse


def index(request):
	lista = ['PL-236-2016','PL-415-2012','PL-349-2014','PL-529-2014','PL-65-2014','PL-209-2011', 'PDL-6-2013', 'PL-254-2010', 'PL-236-2013']
	props = Proposicao.objects.filter(id_prop__in = lista).distinct()
	return render_to_response('index.html', {'props' : props})

def candidato(request):
	form = CandidatoForm()
	return render_to_response('candidato.html', {'form' : form})

def resultado(request, votacao):
	resultado_map = {
		'S' : 1,
		'A' : 0,
		'N' : -1
	}
	votacoes = []
	cmsp = CasaLegislativa.objects.filter(nome_curto = 'cmsp')[0]
	
	lista = ['PL-236-2016','PL-415-2012','PL-349-2014','PL-529-2014','PL-65-2014','PL-209-2011', 'PDL-6-2013', 'PL-254-2010', 'PL-236-2013']
	props = Proposicao.objects.filter(id_prop__in = lista).distinct()
		

	for p in props:
		z = Votacao.objects.filter(proposicao__id = p.id).last()
		votacoes.append(z)
	m_matriz = MatrizesDeDadosBuilder(votacoes, list(cmsp.partidos()), list(cmsp.parlamentares()))
	matriz = m_matriz.gera_matrizes()

	vereadores = []
	for index, parlamentar in enumerate(m_matriz.parlamentares):
		a = matriz[index]
		b = [resultado_map[n] for n in votacao]
		euclides = sqrt(sum( (a - b)**2 for a, b in zip(a, b)))
		vereadores.append({
			'distancia' : euclides,
			'nome' : parlamentar.nome
			})
		vereadores = sorted(vereadores, key=lambda vereador: vereador['distancia'])
	return render_to_response('resultado.html', { 'vereadores' : vereadores })
