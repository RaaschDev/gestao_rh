from django.db import models

class Departamento(models.Model):
    nome = models.CharField('Nome',max_length=155,help_text='Nome do departamento')

    def __str__(self) -> str:
        return self.nome