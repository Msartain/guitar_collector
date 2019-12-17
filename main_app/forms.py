from django.forms import ModelForm
from .models import Restring

class RestringForm(ModelForm):
    class Meta:
        model = Restring
        fields = ['date', 'brand']