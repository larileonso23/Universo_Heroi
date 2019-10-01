from django.db import models
from django.db import models

# Create your models.


class UniversoSerializer(models.model):
    nome = models.CharField(
     
        max_length=50
    )

