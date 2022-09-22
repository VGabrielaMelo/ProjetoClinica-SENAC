from django.db import models

# Create your models here.

# O modelo (models) trata-se de um classe que extende models.Model 
# Este modelo já possui diversos recursos para o uso de banco de dados e interface, como 
#   o atribui id, que cria um identificador único para o registro e o objects, que trata módulo manage que nos possibilita
#   criar comandos de consulta no banco de dados.

# Documentaçã para selecionar os Fields: 

class Especialidade(models.Model):
    codigo = models.PositiveIntegerField()

    nome = models.CharField(
        max_length=255
    )

    descricao = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.nome


class Medico(models.Model):
    # CharField: este tipo de atributo cri no banco de dados um campo de texto (VARCHAR).
    #   É obrigatório a parametrização do tamanho máximo, para isso utilizamos o max_length.

    # Por padrão não é aceito informações nulas nos atributos, para que não seja obrigatório o uso 
    #   de determinado atributo é utilizado o parâmetro null para que no banco de dados seja um NOT NULL 
    #   e blanck para permitir informações em brando na interface. 

    # DataField: tipo do atributo que representa uma data.

    # EmailField: tipo do atributo que representa uma email.
    #   Para o banco de dados é simplesmente um texto, e para a interface em componente
    #   com validação do e-mail.
   
    # Nome 
    nome = models.CharField(
        max_length=255,
    )

    # CPF
    cpf = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )

    # CRM
    crm = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    # Data de Nascimento
    data_nasc = models.DateField(
        null=True,
        blank=True
    )

    # Cidade
    cidade = models.CharField(
        max_length=255,
        null=True,
        blank=True 
    )

    # E-mail
    email = models.EmailField(
        null=True,
        blank=True 
    )

    # Função padrão de classe para transformar uma classe em texto
    def __str__(self):
        return self.nome
