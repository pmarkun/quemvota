from django.shortcuts import render, render_to_response
from django.template import RequestContext
from quiz.models import Proposicao

from .forms import CandidatoForm

# Create your views here.
from django.http import HttpResponse


def index(request):
	props = Proposicao.objects.filter()[0:10]
	return render_to_response('index.html', {'props' : props})

def candidato(request):
	form = CandidatoForm()
	return render_to_response('candidato.html', {'form' : form})