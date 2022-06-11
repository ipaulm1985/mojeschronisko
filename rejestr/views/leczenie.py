from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from rejestr.forms.leczenie import LeczenieCreateForm
from rejestr.forms.leczenie import LeczenieSelect
from rejestr.models import Leczenie


# Create your views here.

class LeczenieCreateView(FormView):
    template_name = 'form.html'
    success_url = reverse_lazy("leczenie")
    form_class = LeczenieCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        Leczenie.objects.create(
            nazwa=data['nazwa'],
        )
        return result


class LeczenieReadView(View):
    def get(self, request):

        return render(request, 'leczenie_read.html', context={'data': Leczenie.objects.all()})


class LeczenieUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy("leczenie")
    model = Leczenie
    form_class = LeczenieCreateForm

class LeczenieSelectDeleteView(FormView):  #skoro nie mam ustawionego delete.html to rowniez moge usunac?
    form_class = LeczenieSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("leczenie_delete", pk=form.cleaned_data['leczenie'].id)


class LeczenieSelectUpdateView(FormView):
    form_class = LeczenieSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("leczenie_update", pk=form.cleaned_data['leczenie'].id)


class LeczenieDeleteView(DeleteView):      #skoro nie mam ustawionego delete.html to rowniez moge usunac?
    template_name = 'leczenie_delete.html'
    model = Leczenie
    success_url = reverse_lazy("leczenie")