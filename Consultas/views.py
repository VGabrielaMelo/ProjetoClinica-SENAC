from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def medicos(request):
    return HttpResponse('Está é a página de médicos.')