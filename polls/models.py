from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model
User = get_user_model()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(
        User,
        editable=False,
        null=True,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def save(self, user = None, *args, **kwargs):
        if self.id is not None and user is not None:
            question_user = QuestionUser.objects.filter(user=user, question=self.question).count()
            if question_user > 0:
                raise ValidationError('Não é permitido votar mais de uma vez')

            question_user = QuestionUser.objects.create(user=user, question=self.question)
            question_user.save()

        super().save(*args, **kwargs)

class QuestionUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

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