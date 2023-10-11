# Django
from django import forms
# Local
from polls.models import Choice # importa o model

# Cria o ModelForm herdando da classe base - *Respeite a indentação*.
class ChoiceModelForm(forms.ModelForm):
    class Meta: # é uma classe mas está dentro do ChoiceModelForm
        # Vincula o model Choice ao Form
        model = Choice
        fields = ('choice_text',)
