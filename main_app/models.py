from django.db import models
from django.urls import reverse

# Create your models here.

class Guitar(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.brand} {self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})