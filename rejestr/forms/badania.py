from django import forms
from rejestr.models import Badania



class BadaniaCreateForm(forms.ModelForm):
    class Meta:
        model = Badania
        fields = '__all__'

    nazwa = forms.CharField(max_length=100)



class BadaniaSelect(forms.Form):
    badania = forms.ModelChoiceField(Badania.objects)