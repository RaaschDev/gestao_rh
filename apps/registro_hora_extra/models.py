from django.db import models

class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=155)

    def __str__(self) -> str:
        return self.motivo

