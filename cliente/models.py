from django.db import models

# Create your models here.

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'cliente'
    
    def __str__(self):
        return self.name