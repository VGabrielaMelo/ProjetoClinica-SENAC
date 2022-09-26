# O módulo views é responsavel por conter todas as funções que retornam informações ao usuário
# Para isso tambem será necessário receber as requisições


# O Django inclui o código das views por padrao a importação do django.shortcuts-render
# Este módulo é responsavel
from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader

from .models import Medico
# Create your views here.
# Por definição as funções de visualização precisam obrigatório ter
# um paramentro de request
def medicos(request):
    #Utilizar o modelo (para este caso Medico) para buscar do banco de dados todos os médicos
    #Pegando todos os medicos de Models
    medicos = Medico.objects.all()

    # Variavel do tipo dicionário que setá responsável por armazenar o contexto que será enviado para o template
    contexto = {'medicos': medicos}

    # Motor de template
    # Preparando o motor do template
    # template = loader.get_template("medicos.html")

    # Já o retorno será uma responsta HTTP para isso será necessário utilizar a função 'HttpResponse'
    # return HttpResponse(template.render(contexto, request))

   # PREPARANDO O TEMPLATE E RETORNA PARA O USUÁRIO COM O CONTEXTO
    # Quando os módulos do shortcut são utilizados é reduzido o volumo de código(ATALHO)
    # No caso render, é necessário colocar como primeiro parâmetro o request(como paramentro da function view), em segundo o template e por ultimo o contexto(conjunto de dados)
    return render(request, 'medicos.html', contexto)