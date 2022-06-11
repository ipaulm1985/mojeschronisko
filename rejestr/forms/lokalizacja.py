
from django import forms
from rejestr.models import Lokalizacja



class LokalizacjaCreateForm(forms.ModelForm):
    class Meta:
        model = Lokalizacja
        fields = '__all__'

    boks = forms.IntegerField(min_value=1, max_value=99)




class LokalizacjaSelect(forms.Form):
    lokalizacja = forms.ModelChoiceField(Lokalizacja.objects)