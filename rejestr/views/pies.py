from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from rejestr.forms.pies import PiesCreateForm
from rejestr.forms.pies import PiesSelect
from rejestr.models import Pies


# Create your views here.

class PiesCreateView(FormView):
    template_name = 'form.html'
    success_url = reverse_lazy("pies")
    form_class = PiesCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        Pies.objects.create(
            nazwa=data['nazwa'],
            rasa=data['rasa'],
            plec=data['plec'],
            wiek=data['wiek']
        )
        return result


class PiesReadView(View):
    def get(self, request):
        Pies.objects.all()
        return render(request, 'pies_read.html', context={'data': Pies.objects.all()})


class PiesUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy("pies")
    model = Pies
    form_class = PiesCreateForm

class PiesSelectDeleteView(FormView):
    form_class = PiesSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("pies_delete", pk=form.cleaned_data['pies'].id)


class PiesSelectUpdateView(FormView):
    form_class = PiesSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("pies_update", pk=form.cleaned_data['pies'].id)


class PiesDeleteView(DeleteView):
    template_name = 'pies_delete.html'
    model = Pies
    success_url = reverse_lazy("pies")