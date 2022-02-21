from django.db import models


class Empresa(models.Model):
    nome = models.CharField('Nome',max_length=155, help_text='Nome da empresa.')

    def __str__(self) -> str:
        return self.nome
