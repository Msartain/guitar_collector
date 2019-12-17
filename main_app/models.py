from django.db import models
from django.urls import reverse

STRINGS = (
    ('Dad', 'Daddario'),
    ('EB', 'Ernie Ball'),
    ('Fen', 'Fender'),
    ('Elx', 'Elixar')
)

GUAGES = (
    ('10-42'),
    ('11-52'),
    ('09-42')
)

class Guitar(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.brand} {self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})
    
    
class Restring(models.Model):
    date = models.DateField('restring date')
    brand = models.CharField(
        max_length=40,
        choices=STRINGS,
        default=STRINGS[0][0]
        )
    # guage = models.CharField(
    #     max_length=30,
    #     choices=GUAGES,
    #     default=GUAGES[0][0]
    #     )
    
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    
    def __str__(self):
         # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_brand_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
