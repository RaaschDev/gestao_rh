from django.db import models

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome do funcionario')

    def __str__(self) -> str:
        return self.nome
