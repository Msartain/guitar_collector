from django.db import models
from django.urls import reverse
from datetime import date

STRINGS = (
    ('Dad', 'Daddario'),
    ('EB', 'Ernie Ball'),
    ('Fen', 'Fender'),
    ('Elx', 'Elixar')
)

class Amp(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    def __str__(self):
        return self.brand
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Guitar(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    amps = models.ManyToManyField(Amp)
    
    def __str__(self):
        return f'{self.brand} {self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})
    
    def restrung_recently(self):
        # we need to get the latest date and filter by it
        # check if that date is more than six months using date.today()
        return self.restring_set.filter(date=date.today())
    
class Restring(models.Model):
    date = models.DateField('restring date')
    brand = models.CharField(
        max_length=40,
        choices=STRINGS,
        default=STRINGS[0][0]
        )
    
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    
    def __str__(self):
         # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_brand_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
