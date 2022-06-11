from django import forms
from rejestr.models import Pies
from rejestr.models import Badania
from rejestr.models import Pies_badania
from rejestr.models import Leczenie
from rejestr.models import Pies_leczenie
from rejestr.models import Dieta
from rejestr.models import Pies_dieta
from rejestr.models import Lokalizacja


class PiesCreateForm(forms.ModelForm):
    class Meta:
        model = Pies
        fields = '__all__'


    nazwa = forms.CharField(max_length=100)
    rasa = forms.CharField(max_length=100)
    plec = forms.CharField(max_length=100)
    wiek = forms.DateField()


class PiesSelect(forms.Form):
    pies = forms.ModelChoiceField(Pies.objects)