# O arquivo urls.py é responsavel por tratar o direcionamento das rotas,
#  conforme a requisões do usuário
from django.urls import path
# importa a view do app
from . import views
# rotas do app

# variável obrigatória
# A variável urlpatterns é uma lista, e a ordem dos itens importam
urlpatterns = [
    # A função path é responsavel por estruturar a rota da aplicação
    path('', views.medicos),
    path('medicos/', views.medicos)
]
