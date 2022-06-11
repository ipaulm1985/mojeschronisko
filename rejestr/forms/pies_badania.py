from django import forms
from rejestr.models import Pies
from rejestr.models import Badania
from rejestr.models import Pies_badania



class Pies_badaniaCreateForm(forms.ModelForm):
    class Meta:
        model = Pies_badania
        fields = '__all__'

    pies = forms.ModelChoiceField(queryset=Pies.objects, required=True)   #queryset może być nie musi, required rownież, true jest w domyśle
    badania = forms.ModelChoiceField(Badania.objects, required=True)
    data_badania = forms.DateField()


class Pies_badaniaSelect(forms.Form):
    pies_badania = forms.ModelChoiceField(Pies_badania.objects)