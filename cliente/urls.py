from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.listar_clientes,
        name='listar_clientes'
    ),

    path(
        'criar/',
        views.criar_cliente,
        name='criar_cliente'
    ),

    path(
        'editar/<int:id>/',
        views.editar_cliente,
        name='editar_cliente'
    ),

    path(
        'excluir/<int:id>/',
        views.excluir_cliente,
        name='excluir_cliente'
    ),
]