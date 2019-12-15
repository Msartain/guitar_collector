from django.db import models

# Create your models here.

class Guitar(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.brand} {self.model} ({self.id})'