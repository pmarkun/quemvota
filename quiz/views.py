from django.shortcuts import render, render_to_response
from django.template import RequestContext


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html', {})