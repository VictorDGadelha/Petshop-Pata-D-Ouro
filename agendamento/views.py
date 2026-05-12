from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Agendamento

def criar_agendamento(request):
    if request.method == 'POST':
        pet = request.POST.get('pet')
        cliente = request.POST.get('cliente')
        servico = request.POST.get('servico')
        produto = request.POST.get('produto')
        data_hora_agendamento = request.POST.get('data_hora_agendamento')
        
        Agendamento.objects.create(
            pet_id=pet,
            cliente_id=cliente,
            servico_id=servico,
            produto_id=produto,
            data_hora_agendamento=data_hora_agendamento
        )
        return redirect('listar_agendamentos')
    return render(request, 'criar_agendamento.html')

def listar_agendamentos(request):
    agendamento = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamento': agendamento})

def editar_agendamento(request, id_agendamento):
    agendamento = get_object_or_404(Agendamento, id_agendamento)
    if request.method == 'POST':
        agendamento.pet_id = request.POST.get('pet')
        agendamento.cliente_id = request.POST.get('cliente')
        agendamento.servico_id = request.POST.get('servico')
        agendamento.produto_id = request.POST.get('produto')
        agendamento.data_hora_agendamento = request.POST.get('data_hora_agendamento')
        agendamento.save()
        return redirect('listar_agendamentos')
    return render(request, 'editar_agendamento.html', {'agendamento': agendamento})

def excluir_agendamento(request, id_agendamento):
    agendamento = get_object_or_404(Agendamento, id_agendamento)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('listar_agendamentos')
    return render(request, 'excluir_agendamento.html', {'agendamento': agendamento})
