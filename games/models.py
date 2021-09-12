from django.db import models

# Create your models here.

class Games(models.Model):
    """Modelo de referencia para a tabela Games."""
    numero_sorteio = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    numeros_ganhadores = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.numero_sorteio) + " - " + str(self.data)