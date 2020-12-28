from django.urls import path
from .views import listarnovels,tablenovels,salvar_novel,delete_novel,update_novels

urlpatterns = [
    path('', listarnovels, name='estante'),
    path('tabela', tablenovels, name='painel'),
    path('newnovel',salvar_novel, name='adicionarnovel'),
    path('deletarnovel/<int:id>',delete_novel,name='deletarnovel'),
    path('updatenovel/<int:id>',update_novels,name='alterarnovel'),
]
