from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import cliente

def criar_cliente(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        cliente.objects.create(
            name_cliente=name,
            age_cliente=age,
            email_cliente=email,
            address_cliente=address
        )
        return redirect('listar_clientes')
    return render(request, 'cliente/criar_cliente.html')

def listar_clientes(request):
    listagem_clientes = cliente.objects.all()
    return render(request, 'cliente/listar_clientes.html', {'clientes': listagem_clientes})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.name = request.POST.get('name')
        cliente.age = request.POST.get('age')
        cliente.email = request.POST.get('email')
        cliente.address = request.POST.get('address')
        cliente.save()
        return redirect('listar_clientes')

    return render(request, 'cliente/editar_cliente.html', {'cliente': cliente})

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'cliente/excluir_cliente.html', {'cliente': cliente})




# Create your views here.
