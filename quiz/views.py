from __future__ import division

import json
from itertools import groupby, chain

from django.shortcuts import render_to_response

from .models import Proposicao, CasaLegislativa, Votacao, Voto, Parlamentar
from .utils import MatrizesDeDadosBuilder
from .forms import CandidatoForm


PLS = ['PL-17-2017','PL-318-2017', 'PL-566-2017', 'PL-477-2018', 'PL-615-2018', 'PL-626-2018', 'PL-641-2018', 'PL-117-2019', 'PL-324-2017', 'PL-274-2018', 'PL-539-2019', 'PL-207-2020', 'PL-217-2020', 'Pl-452-2020', 'PL-84-2019', 'PL-620-2016']

PROPOSTA_URL = "https://splegisconsulta.camara.sp.gov.br/Pesquisa/DetailsDetalhado?COD_MTRA_LEGL=1&ANO_PCSS_CMSP={p.ano}&COD_PCSS_CMSP={p.numero}"

def index(request):
    propostas = Proposicao.objects.filter(id_prop__in=PLS).distinct()
    
    propdata = [{'nome': '{p.sigla} {p.numero}/{p.ano}'.format(p=proposta),
                 'url': PROPOSTA_URL.format(p=proposta),
                 'ementa': proposta.ementa,
                 'hashtags' : proposta.hashtags,
                 'uservote': None} for proposta in propostas]


    parlamentares = []
    for parlamentar in Parlamentar.objects.all():
        votos = []
        for proposta in propostas:
            voto = parlamentar.voto_set.filter(votacao__proposicao=proposta)
            if voto:
                if voto.first().opcao == 'SIM':
                    votos.append(1)
                elif voto.first().opcao == 'NAO':
                    votos.append(-1)
            else:
                votos.append(0)
        
        p = {'nome': parlamentar.nome,
                      'partido': parlamentar.partido.nome,
                      'numero' : parlamentar.numero,
                      'url' : parlamentar.url,
                      'votos': votos,
                      'image': '/static/media/fotovereadores/' + parlamentar.nome.lower() + '.jpg'}
        parlamentares.append(p)

    return render_to_response('index.html',
                              {'propostas' : propostas,
                               'propdata': json.dumps(propdata),
                               'parldata': json.dumps(parlamentares)})

def candidato(request):
    form = CandidatoForm()
    return render_to_response('candidato.html', {'form' : form})

def resultado(request, votacao):
    pass
