from django.db import models

class Documento(models.Model):
    descricao = models.CharField('Descricao', max_length=100)

    def __str__(self) -> str:
        return self.descricao