from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Amp
from .forms import RestringForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    amps_guitar_doesnt_have = Amp.objects.exclude(id__in = guitar.amps.all().values_list('id'))
    restring_form = RestringForm()
    return render(request, 'guitars/detail.html', { 
        'guitar' : guitar,
        'restring_form': restring_form,
        'amps': amps_guitar_doesnt_have
        })
    

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'
    
class GuitarUpdate(UpdateView):
    model = Guitar
    fields = '__all__'
    
class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'
    
def add_restring(request, guitar_id):
    form = RestringForm(request.POST)
    if form.is_valid():
        # don't save the form to the db until it has the guitar_id assigned
        new_restring = form.save(commit=False)
        new_restring.guitar_id = guitar_id
        new_restring.save()
        return redirect('detail', guitar_id=guitar_id)
    
def assoc_amp(request, guitar_id, amp_id):
    Guitar.objects.get(id=guitar_id).amps.add(amp_id)
    return redirect('detail', guitar_id=guitar_id)

def unassoc_amp(request, guitar_id, amp_id):
    Guitar.objects.get(id=guitar_id).amps.remove(amp_id)
    return redirect('detail', guitar_id=guitar_id)
    
class AmpList(ListView):
  model = Amp

class AmpDetail(DetailView):
  model = Amp

class AmpCreate(CreateView):
  model = Amp
  fields = '__all__'

class AmpUpdate(UpdateView):
  model = Amp
  fields = ['brand', 'model']

class AmpDelete(DeleteView):
  model = Amp
  success_url = '/amps/'