from django.db import models

# Create your models here.
class Parametro(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    valor = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'parametro'