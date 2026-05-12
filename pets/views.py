from django.shortcuts import render
from django.shortcuts import redirect   
from django.shortcuts import get_object_or_404

from .models import Pets

def criar_pet(request):
    if request.method == 'POST':
        nome_pet = request.POST.get('nome_pet')
        especie_pet = request.POST.get('especie_pet')
        idade_pet = request.POST.get('idade_pet')
        peso_pet = request.POST.get('peso_pet')
        dono_id = request.POST.get('dono_id')

        Pets.objects.create(
            nome_pet=nome_pet,
            especie_pet=especie_pet,
            idade_pet=idade_pet,
            peso_pet=peso_pet, 
            dono_id=dono_id
        )
        return redirect('listar_pets')
    return render(request, 'criar_pet.html')

def listar_pets(request):
    listar_pets = Pets.objects.all()
    return render(request, 'listar_pets.html', {'listar_pets': listar_pets})

def editar_pet(request, id_pet):
    Pets = get_object_or_404(Pets, id_pet=id_pet)
    if request.method == 'POST':
        Pets.nome_pet = request.POST.get('nome_pet')
        Pets.especie_pet = request.POST.get('especie_pet')
        Pets.idade_pet = request.POST.get('idade_pet')
        Pets.peso_pet = request.POST.get('peso_pet')
        Pets.dono_id = request.POST.get('dono_id')
        Pets.save()
        return redirect('listar_pets')
    return render(request, 'editar_pet.html', {'Pets': Pets})

def excluir_pet(request, id_pet):
    Pets = get_object_or_404(Pets, id_pet=id_pet)
    if request.method == 'POST':
        Pets.delete()
        return redirect('listar_pets')
    return render(request, 'excluir_pet.html', {'Pets': Pets})   


