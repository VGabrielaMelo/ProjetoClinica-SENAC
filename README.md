# Django
Projeto do curso de Django

A proposta deste projeto é construir uma aplicação web para atender uma clinica

O objetibo é desenvolver as seguintes telas:

- Médicos
- Especialidades
- Procedimentos
- Consultas

## Preparar o ambiente

- Instalação do venv

```
python -m venv venv
```

- Ativar o ambiente virtual (venv)

```
.\venv\Scripts\activate.bat
```

- Instalação do Django

```
pip install django
```

- Colocando as versões do pacote em um arquivo .txt (Comando opcional)

```
pip freeze > requirents.txt
```

## Estruturação do Projeto 
1. Criar o projeto 
NOTE: Projeto é o local que o motor do DJango é executado, com isso as configurações são feitas dentro dele, 
utilizando o arquivo settings.py. 

```
django-admin startproject -nome do projeto- .
```

- django-admin: comando de terminal responsável pela administração do DJango
- startproject: parametro do comando django-admin responsável por estruturar um projeto em DJango.
    É obrigatório informar o nome do projeto (neste caso "clinica").
    Como próximo parâmetro é o diretório que será estruturado o projeto, que a sugestão é informar o caminho relatório
    do diretório local ".".

## Iniciar o serviço web
```
python -m manage runserver
```
- manage: módulo do DJango responsável por executar ações dentro do projeto.
- runserver: parâmetro que determina a execução do módulo web disponível dentro do DJango para desenvolvimento.

O site estará disponível no endereço http://127.0.0.1:8000/

2. Criar um APP
NOTE: o APP (aplicação) será o local no DJango que será implementado toda a lógica. Lembrando que um projeto pode ser
vários APPs. 

```
python -m manage startapp -nome da pasta-
```

- Clinica: pasta que contem os arquivos do projeto.
- Consultas: pasta que trata os arquivos da aplicação.

## Adicionando o APP ao projeto
É necessário entrar no arquivo settings.py e localizar a constante "INSTALLED_APPS".
A constante "INSTALLED_APPS" é uma lista que contem todos os APPs associados ao projeto, somente após um APP estar 
relacionado nesta lista que o DJango pode identificar e utilizar o APP nos demais fins. 

Verificando os SQLs do migrations

```
python -m manage sqlmigrate consultas 0001
```

> IMPORTANTE: configurar o TIME_ZONE para que a aplicação seja executade com o horário local. 


> Configurar a linguagem da aplicação no LANGUAGE_CODE
```
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"
```

## Registrar o APP á aplicação admin
A aplicação admin é uma interface gerada de maneira automática pelo DJango, que utiliza o modelo desenvolvido na aplicação, para
criar uma interface básica de gestão, ou seja, uma tela de lista, detalhes, inclusão, atuaçização e exclusão.

```
C -> Create (Criar)
R -> Read (Ler)
U -> Update (Atualizar)
D -> Delete (Excluir)
```

Para registrar a aplicação é necessário localizar o arquivo consultas/admin.py e incluir os comandos de registros do modelo.

## Cadastrar o super usuário (admin)
Para acessar a tela de admin é necessário que se tenha um usuáriodevidamente registrado na aplicação.

```
python -m manage createsuperuser
```

- createsuperuser: é o comando utilizado para criar o usuário administrativo da aplicação.

## Migration 
O migration (migrações) é o ato de capturar o modelo de dados desenvolvimento em uma camada de aplicação, é preprarar os códigos necessários para criar o banco de dados.

> IMPORTANTE: o migrate não está vinculado a nenhum banco de dados específico   

```
python -m manage makemigrations consultas
```

- makemigrations: é o comando responsável pela preparação do modelo que será implantado no banco de dados.
    - como parâmetro é necessário informar o nome da aplicação.

Após a execução deste comando, a pasta migrations é criada dentro da aplicação (consultas/migrations)

- migrate: é o comando responsável por aplicar a estrutura criado pelo makemigration.
```
python -m manage migrate consultas
```