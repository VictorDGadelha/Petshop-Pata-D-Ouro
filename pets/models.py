from django.db import models

class Pets(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome_pet = models.CharField(max_length=100)
    especie_pet = models.CharField(max_length=100)
    idade_pet = models.IntegerField()
    peso_pet = models.FloatField()
    dono = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'pets'
    
    def __str__(self):
        return self.nome_pet    
