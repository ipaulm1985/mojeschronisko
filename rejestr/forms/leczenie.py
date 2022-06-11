from django import forms
from rejestr.models import Leczenie



class LeczenieCreateForm(forms.ModelForm):
    class Meta:
        model = Leczenie
        fields = '__all__'

    nazwa = forms.CharField(max_length=100)



class LeczenieSelect(forms.Form):
    leczenie = forms.ModelChoiceField(Leczenie.objects)