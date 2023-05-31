from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

# em caso de erro fatal no servidor
# corrigir o erro
# executar CTRL + C no terminal
# executar o servidor novamente python manage.py runserver
