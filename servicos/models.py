from django.db import models

class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    tipo_servico = models.CharField(max_length=100, null=False)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    data_hora_agenda = models.DateTimeField()
    class Meta:
        db_table = "servicos"
    
    def __str__(self):
        return self.tipo_servico     

