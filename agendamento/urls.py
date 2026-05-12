from django.urls import path
from . import views

urlpatterns = [ path(
        '',
        views.listar_agendamentos,
        name='listar_agendamentos'
    ),

    path(
        'criar/',
        views.criar_agendamento,
        name='criar_agendamento'
    ),

    path(
        'editar/<int:id>/',
        views.editar_agendamento,
        name='editar_agendamento'
    ),

    path(
        'excluir/<int:id>/',
        views.excluir_agendamento,
        name='excluir_agendamento'
    ),
]