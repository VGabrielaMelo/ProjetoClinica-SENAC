from django.db import models

# O modelo(models) trata-se de uma classe que extends models.Model
# Este models já possui diversos recursos para o uso de banco de dados e interfaces.
# Como atribui id, que cria um identificador unico para o registro e o objects, que
# trata modulo manage que nos possibilita criar comandos de consulta no banco de de dados

# Documentação para selecionar os Fields
# https://docs.djangoproject.com/en/4.1/ref/models/fields/

class Especialidades(models.Model):
    codigo = models.AutoField(
        primary_key=True
    )

    nome = models.CharField(
        max_length = 255
    )

    descricao = models.CharField(
        max_length = 1000,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nome

class Medico(models.Model):
    # CharField: este tipo de atributo cria no banco de dados um campo de texto (VARCHAR)
    # É obrigatório a parametrização do tamanho máximo, para isso utilizamos o max_lenght

    nome = models.CharField(
        max_length=255
    )

    # Por padrão não é aceito informações nulas nos atributos, para que não seja obrigatório
    # O uso de determinada atributo é utilizado o parametro 'null' para que no banco de dados
    # seja um 'not null' e 'blank' para permitir informações em branco na interface.

    cpf = models.CharField(
        max_length = 11,
        null = True,
        blank = True
    )

    crm = models.CharField(
        max_length = 10,
        null = True,
        blank = True
    )

    # DateField: tipo de atributo que representa uma data
    data_nascimento = models.DateField(
        null = True,
        blank = True,
    )

    cidade = models.CharField(
        max_length = 255,
        null = True,
        blank = True
    )

    # EmailField: tipo que representa um e-mail
    # Para o banco de dados é simplesmente um texto, e para a interface um componente
    # Com validação do e-mail.
    email = models.EmailField()

    uf = models.CharField(
    max_length=2,
    null=True,
    blank=True
    )

    # Dentro tipos disponibilizados pelo Model Fields é possivel localizar o
    # tipo foreignKey (chave estrangeira), sendo assim o proprio Django se reponsabiliza em estruturar o modelo de dados
    especialidade = models.ForeignKey(
        Especialidades,
        # ele não deixa que a especilidade seja apaga se ela já estiver vinculada a um medico
        on_delete=models.PROTECT
    )

    # Função padrão de classe para transformar uma classe em texto
    def __str__(self):
        return self.nome

class Procedimentos(models.Model):
    codigo = models.AutoField(
        primary_key=True
    )

    nome = models.CharField(
        max_length=255
    )

    descricao = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

class Consultas(models.Model):
    codigo = models.AutoField(
        primary_key=True
    )

    data = models.DateField()

    medico = models.ForeignKey(
        Medico,
        on_delete=models.PROTECT
    )

    laudo = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    procedimentos = models.ManyToManyField(
        Procedimentos
    )

    def __str__(self):
        return f"Consulta {self.codigo}"

