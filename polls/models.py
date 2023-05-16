from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# ativar o ambiente virtual
""" 
No terminal
    python manage.py migrate

    Configurar o módulo polls para ser utilizado no projeto
      No arquivos my_site/settings.py incluir o módulo polls 
      como um INSTALLED_APPS

    python manage.py makemigrations
    python manage.py migrate
"""