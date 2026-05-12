from django.db import models

class clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=150)
    cpf_cliente = models.CharField(max_length=20, unique=True)
    tel_cliente = models.CharField(max_length=20)
    email_cliente = models.CharField(max_length=100)
    endereco_cliente = models.TextField()
    class Meta:
        db_table = "clientes"

class pets(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome_pet = models.CharField(max_length=100)
    especie_pet = models.CharField(max_length=50)
    cor_pet = models.CharField(max_length=50)
    peso_pet = models.DecimalField(max_digits=5, decimal_places=2)
    dono = models.ForeignKey('clientes', on_delete=models.CASCADE, db_column='dono_id')
    class Meta:
        db_table = "pets"

class servicos(models.Model):
    id_servico = models.AutoField(primary_key=True)
    tipo_servico = models.CharField(max_length=100)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = "servicos"

class agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_agendamento = models.DateTimeField()
    pet = models.ForeignKey('pets', on_delete=models.CASCADE)
    servico = models.ForeignKey('servicos', on_delete=models.CASCADE)
    class Meta:
        db_table = "agendamentos"

class produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    categoria_produto = models.CharField(max_length=50)
    valor_produto = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    class Meta:
        db_table = "produtos"

class venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey('clientes', on_delete=models.CASCADE)
    class Meta:
        db_table = "venda"

class item_venda(models.Model):
    id_item = models.AutoField(primary_key=True)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    venda = models.ForeignKey('venda', on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos', on_delete=models.CASCADE)
    class Meta:
        db_table = "item_venda"

class petshop(models.Model):
    id_petshop = models.AutoField(primary_key=True)
    nome_loja = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    endereco_loja = models.TextField()
    telefone_loja = models.CharField(max_length=20)
    class Meta:
        db_table = "petshop"