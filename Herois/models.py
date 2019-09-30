from django.db import models

# Create your models here.

class HeroisSerializer(models.Model):
    nome = models.CharField(
        max_length=55
    )