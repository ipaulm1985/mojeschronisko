from django import forms
from rejestr.models import Dieta



class DietaCreateForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'

    nazwa = forms.CharField(max_length=100)



class DietaSelect(forms.Form):
    dieta = forms.ModelChoiceField(Dieta.objects)