from __future__ import division

import json
from itertools import groupby, chain

from django.shortcuts import render_to_response

from .models import Proposicao, CasaLegislativa, Votacao, Voto
from .utils import MatrizesDeDadosBuilder
from .forms import CandidatoForm


PLS = ['PL-749-2019', 'PL-167-2017', 'PL-522-2018', 'PL-613-2019', 'PR-14-2001', 'PL-667-2015', 'PL-615-2018', 'PL-308-2020', 'PL-613-2017', 'PL-630-2017', 'PL-596-2018', 'PL-252-2020', 'PL-620-2016']
PLS = ['PL-318-2017', 'PL-566-2017', 'PL-477-2018', 'PL-615-2018', 'PL-626-2018', 'PL-641-2018', 'PL-117-2019', 'PL-324-2017', 'PL-274-2018', 'PL-539-2019', 'PL-207-2020', 'PL-217-2020', 'Pl-452-2020', 'PL-84-2019', 'PL-620-2016']

PROPOSTA_URL = "https://splegisconsulta.camara.sp.gov.br/Pesquisa/DetailsDetalhado?COD_MTRA_LEGL=1&ANO_PCSS_CMSP={p.ano}&COD_PCSS_CMSP={p.numero}"

def index(request):
    propostas = Proposicao.objects.filter(id_prop__in=PLS).distinct()
    #proposta_random = Proposicao.objects.order_by('?')[:1]
    #propostas = list(chain(propostas,proposta_random))
    PROPOSTAS = propostas.values_list('id_prop', flat=True)
    propdata = [{'nome': '{p.sigla} {p.numero}/{p.ano}'.format(p=proposta),
                 'url': PROPOSTA_URL.format(p=proposta),
                 'ementa': proposta.ementa,
                 'hashtags' : proposta.hashtags,
                 'uservote': None} for proposta in propostas]

    votacoes = Votacao.objects.filter(proposicao__id_prop__in=PROPOSTAS).order_by('id')
    votacoes = [max(group, key=lambda v: v.id)
                for _, group
                in groupby(votacoes, key=lambda v: v.proposicao_id)]


    cmsp = CasaLegislativa.objects.get(nome_curto='cmsp')
    builder = MatrizesDeDadosBuilder(votacoes, cmsp.partidos(), cmsp.parlamentares())
    matriz = builder.gera_matrizes()

    parlamentares = [{'nome': parlamentar.nome,
                      'partido': parlamentar.partido.nome,
                      'votos': list(votos),
                      'image': '/static/media/fotovereadores/' + parlamentar.nome.lower() + '.jpg'}
                     for parlamentar, votos
                     in zip(builder.parlamentares, matriz)
                     if not all(voto == 0.0 for voto in votos)]

    return render_to_response('index.html',
                              {'propostas' : propostas,
                               'propdata': json.dumps(propdata),
                               'parldata': json.dumps(parlamentares)})

def candidato(request):
    form = CandidatoForm()
    return render_to_response('candidato.html', {'form' : form})

def resultado(request, votacao):
    pass
