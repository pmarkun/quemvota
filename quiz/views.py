from __future__ import division

import json
from itertools import groupby

from django.shortcuts import render_to_response

from .models import Proposicao, CasaLegislativa, Votacao, Voto
from .utils import MatrizesDeDadosBuilder
from .forms import CandidatoForm


PROPOSTAS = ['PL-236-2016', 'PL-415-2012', 'PL-349-2014',
             'PL-529-2014', 'PL-65-2014', 'PL-209-2011',
             'PDL-6-2013', 'PL-254-2010', 'PL-236-2013']

PROPOSTA_URL = ('http://documentacao.camara.sp.gov.br/'
                'cgi-bin/wxis.exe/iah/scripts/'
                '?IsisScript=iah.xis&lang=pt&format=detalhado.pft'
                '&base=proje&form=A&nextAction=search&'
                'indexSearch=^nTw^lTodos%20os%20campos&exprSearch=P=')

def index(request):
    propostas = Proposicao.objects.filter(id_prop__in=PROPOSTAS).distinct()
    propdata = [{'nome': '{p.sigla} {p.numero}/{p.ano}'.format(p=proposta),
                 'url': PROPOSTA_URL + '{p.sigla}{p.numero}{p.ano}'.format(p=proposta),
                 'ementa': proposta.ementa,
                 'uservote': None} for proposta in propostas]

    votacoes = Votacao.objects.filter(proposicao__id_prop__in=PROPOSTAS).order_by('id')
    print votacoes
    votacoes = [max(group, key=lambda v: v.id)
                for _, group
                in groupby(votacoes, key=lambda v: v.proposicao_id)]


    cmsp = CasaLegislativa.objects.get(nome_curto='cmsp')
    builder = MatrizesDeDadosBuilder(votacoes, cmsp.partidos(), cmsp.parlamentares())
    matriz = builder.gera_matrizes()

    parlamentares = [{'nome': parlamentar.nome,
                      'partido': parlamentar.partido.nome,
                      'votos': list(votos)}
                     for parlamentar, votos
                     in zip(builder.parlamentares, matriz)]

    return render_to_response('index.html',
                              {'propostas' : propostas,
                               'propdata': json.dumps(propdata),
                               'parldata': json.dumps(parlamentares)})

def candidato(request):
    form = CandidatoForm()
    return render_to_response('candidato.html', {'form' : form})

def resultado(request, votacao):
    pass
