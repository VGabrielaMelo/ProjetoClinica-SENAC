from django.contrib import admin

# Register your models here.

# Importar o módulo(models) criado dentro no arquivo models.py 
# Sendo assim é necessário a utilização do .models visto que models é o nome do módulo e o ".", é 
#   a estrutura do pacote (packge).
from .models import Especialidades, Procedimentos, Medico, Consultas

# O registro é feito através do módulo contrib, previamente importado pelo Django.
# Para acontecer o registro é necessário dentro do atributo "site" executar o método
#   "register" passando por parâmetro o modelo, para este caso medico. 
admin.site.register(Medico)

admin.site.register(Procedimentos)

admin.site.register(Especialidades)

admin.site.register(Consultas)
