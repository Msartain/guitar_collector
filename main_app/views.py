from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Guitar:
    def __init__(self, brand, model, description, year):
        self.brand = brand
        self.model = model
        self.description = description
        self.year = year
        
guitars = [
    Guitar('Gibson', 'ES125', 'pickguard missing and headstock repair', 1951),
    Guitar('Fender', 'Musicmaster', 'Red with White scratchplate', 1974),
    Guitar('Fender', 'P-Bass', 'Honey blonde with gold metal scratch plate', 2018),
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
  return render(request, 'guitars/index.html', { 'guitars': guitars })