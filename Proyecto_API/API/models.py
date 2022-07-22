from django.db import models
from django.db.models import Model

class Peliculas(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Title= models.CharField(max_length=100)
    Duration= models.DurationField()
    Premiere= models.DateTimeField()
