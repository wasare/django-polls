from django.urls import path

# importar da pasta atual o arquivo views.py
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
    path('perguntas/list', views.ultimas_perguntas, name='polls_list'),
    path('pergunta/add', views.QuestionCreateView.as_view(), name="poll_add"),
    path('pergunta/<int:pk>/edit',
              views.QuestionUpdateView.as_view(),
              name="poll_edit"
    ),
    path('pergunta/<int:pk>/delete',
              views.QuestionDeleteView.as_view(),
              name="poll_delete"
    ),

]

# .\venv\Scripts\activate.bat
# python manage.py runserser