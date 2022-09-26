# Django
Projeto feito com Django

A proposta deste projeto é construir uma aplicação web irá atender uma clinica

O objetivo é desenvolver as seguintes telas:

- Médicos
- Especialidades
- Procedimentos
- Consultas

## Preparar o ambiante
- Instalando o venv
```
    python -m venv venv
```

- Ativando o venv
```
    .\venv\script\activate
```

- Instalação do Django
```
    pip install django
```

- (OPCIONAL) Colocando as versões do pacote em um arquivo .txt
```
    pip freeze > requirents.txt
```

## Estruturação do Projeto
1. Criar o projeto
> NOTE: Projeto é o local que o motor do Django é executado, com isso as configurações são feitas dentro dele, utilizando o arquivo settings.py

```
   django-admin startproject (nome-do-projeto) .
```

- django-admin: comando de terminal responsável pela administração do Django
- startproject: Parametro do comando django-admin responsável por estruturar um projeto em django
    È obrigatório o nome do projeto (neste caso "clinica")
    Como proximo parametro é o diretório que será executado o projeto, que a sugestão é informar o caminho relativo do diretório local "."

## Iniciar o serviço web
```
    python -m manage runserver
```

- manage: Módulo do Django responsável por executar ações dentro do projeto
- runserver: Parametro que determina a execução do módulo web disponível dentro do Django para desenvolvimento

O site estará disponivel no endereço "http://127.0.0.1:8000/"

2. Criar um APP
> NOTE: O APP (aplicação) será o local no Django que setá implementado toda a lógica. Lembrando que um projeto pode ter vários APPs.

```
   python -m manage startapp consultas
```

clinica: pasta que contem os arquivos do projeto
consultas: pasta que trata os arquivos da aplicação

## Adicionando o APP ao Projeto
È necessário entrar no arquivo settings.py e localizar a constante "INSTALLED_APPS".
A contante "INSTALLED_APPS" é uma lista que contem todos os APPs associados ao projeto, somente após um APP estar relacionado nesta lista que o Django pode identificar e utilizar o APP nos demais fins.

fazendo um migration

```
    python -m manage migrations consultas
```

verificando os SQLs do migrations

```
    python -m manage sqlmigrate consultas 0001
```

> IMPORTANTE: configure o TIME_ZONE para que aplicação seja executada com o horário local
> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
> Configurar o linguagem da aplicação no LANGUAGE_CODE
> http://www.i18nguy.com/unicode/language-identifiers.html

> Configurar a linguagem da aplicação no LANGUAGE_CODE

```
    LANGUAGE_CODE = 'pt_br'

    TIME_ZONE = 'America/Sao_Paulo'
```

## Registrar o APP a aplicação admin
A aplicação admin é uma interface gerada de maneira automática pelo Django, que utiliza o modelo desenvolvido na aplicação, para criar uma interface básica de gestão, ou seja uma tela de lista, detalhes, inclusão, atualização, exclusão.

```
C => Create (Criar)
R => Read (Ler)
U => Update (Atualizar)
D => Delete (Excluir)
```

Para registrar a aplicação é necessário o arquivo consultas/admin.py e incluir os comandos de registro do modelo(MODELS)

## Cadastrar o super usuário (admin)
Para acessar a tela de admin é necessário que se tenha um usuário devidamente registrado na aplicação

```
    python -m manage createsuperuser 
```

- createsuperuser: é o comando utilizado para criar o usuário administrativo da aplicação

## Migration
O migration (migrações) é o ato da capturar o modelo de dados desenvolvido em uma camada de aplicação, a preparar os códigos necessários para criar o banco de dados.

> IMPORTANTE: O migrate não está vinculado a nenhum banco de dados especifico

```
    python -m manage makemigrations consultas
```

- makemigrations: é o comando responsavel pela preparacao do modelo que sera implementdo no banco de dados.
    como parametro é necessário informar o nome da aplicação

Após a execução deste comando, a pasta migrations e criada dentro da aplicação (consulta/migrations)

- migrate: é o comando responsavel por aplicar a estrutura criada pelo makemigration

```
    python -m manage migrate consultas
```
## URLconf
A URLconf é um termo utilizado para tratar as arquivos url.py. Este arquivo está presente no projeto e na aplicação

O comando startapp não cria o arquivo url.py na aplicação, a necessário criar o arquivo.

> IMPORTANTE: O arquivo deve contar obrigatoriamente uma variável chamada urlpatterns