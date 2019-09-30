from django.db import models

# Create your models here.

class UniversoSerializer(models.model):
    nome = models.CharField(
        max_length=55
    )

