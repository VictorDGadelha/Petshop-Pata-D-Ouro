from django.urls import path
from . import views 

urlpatterns = [
    path(
        '',
        views.listar_pets,
        name='listar_pets'
    ),

    path(
        'criar/',
        views.criar_pet,
        name='criar_pet'
    ),

    path(
        'editar/<int:id>/',
        views.editar_pet,
        name='editar_pet'
    ),

    path(
        'excluir/<int:id>/',
        views.excluir_pet,
        name='excluir_pet'
    ),

]