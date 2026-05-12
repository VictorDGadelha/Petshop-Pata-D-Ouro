from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Servico

def criar_servico(request):
    if request.method == "POST":
        tipo_servico = request.POST.get("tipo_servico")
        valor_servico = request.POST.get("valor_servico")
        data_hora_agenda = request.POST.get("data_hora_agenda")
        
        Servico.objects.create(
            tipo_servico=tipo_servico,
            valor_servico=valor_servico,
            data_hora_agenda=data_hora_agenda
        )
        return redirect("listar_servicos")
    return render(request, "servicos/criar_servico.html")

def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, "servicos/listar_servicos.html", {"servicos": servicos})

def editar_servico(request, id_servico):
    servico = get_object_or_404(Servico, id_servico=id_servico)
    if request.method == "POST":
        servico.tipo_servico = request.POST.get("tipo_servico")
        servico.valor_servico = request.POST.get("valor_servico")
        servico.data_hora_agenda = request.POST.get("data_hora_agenda")
        servico.save()
        return redirect("listar_servicos")
    return render(request, "servicos/editar_servico.html", {"servico": servico})

def excluir_servico(request, id_servico):
    servico = get_object_or_404(Servico, id_servico=id_servico)
    if request.method == "POST":
        servico.delete()
        return redirect("listar_servicos")
    return render(request, "servicos/excluir_servico.html", {"servico": servico})

