from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField('Descricao', max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.descricao