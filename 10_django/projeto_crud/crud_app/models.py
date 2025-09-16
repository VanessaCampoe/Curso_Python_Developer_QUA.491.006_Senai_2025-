from django.db import models

# Create your models here.
#  vamos manter esse import como esta aquimsem nenhum pb 


class Pessoa(models.Model):  # Moldel e a class da importação models
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False) # max_length ele e espanssivo e economiza espaço 
    email = models.EmailField(unique=True, null=False, blank=False) # unique campoe em branco ... null=False, blank=False)
    cpf = models.CharField(max_length=14,unique=True, null=True, blank=True)           #// equivalente ao varchar 
   