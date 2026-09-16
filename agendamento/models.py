from django.db import models
from django.utils import timezone

#titulo, data, hora, user, criado em, descrição

class Agendamento(models.Model):
    tittle = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.tittle} - {self.date}'