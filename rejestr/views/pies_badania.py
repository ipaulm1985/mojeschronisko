from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from rejestr.forms.pies_badania import Pies_badaniaCreateForm
from rejestr.forms.pies_badania import Pies_badaniaSelect
from rejestr.models import Pies_badania


# Create your views here.

class Pies_badaniaCreateView(FormView):
    template_name = 'form.html'
    success_url = reverse_lazy("pies_badania")
    form_class = Pies_badaniaCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        Pies_badania.objects.create(
            pies=data['pies'],
            badania=data['badania'],
            data_badania=data['data_badania']
        )
        return result


class Pies_badaniaReadView(View):
    def get(self, request):

        return render(request, 'pies_badania_read.html', context={'data': Pies_badania.objects.all()})


class Pies_badaniaUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy("pies_badania")
    model = Pies_badania
    form_class = Pies_badaniaCreateForm

class Pies_badaniaSelectDeleteView(FormView):
    form_class = Pies_badaniaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("pies_badania_delete", pk=form.cleaned_data['pies_badania'].id)


class Pies_badaniaSelectUpdateView(FormView):
    form_class = Pies_badaniaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("pies_badania_update", pk=form.cleaned_data['pies_badania'].id)


class Pies_badaniaDeleteView(DeleteView):
    template_name = 'pies_badania_delete.html'
    model = Pies_badania
    success_url = reverse_lazy("pies_badania")