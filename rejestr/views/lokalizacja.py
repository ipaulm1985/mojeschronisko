from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from rejestr.forms.lokalizacja import LokalizacjaCreateForm
from rejestr.forms.lokalizacja import LokalizacjaSelect
from rejestr.models import Lokalizacja


# Create your views here.

class LokalizacjaCreateView(FormView):
    template_name = 'form.html'
    success_url = reverse_lazy("lokalizacja")
    form_class = LokalizacjaCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        Lokalizacja.objects.create(
            nazwa=data['boks'],
        )
        return result


class LokalizacjaReadView(View):
    def get(self, request):

        return render(request, 'lokalizacja_read.html', context={'data': Lokalizacja.objects.all()})


class LokalizacjaUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy("lokalizacja")
    model = Lokalizacja
    form_class = LokalizacjaCreateForm

class LokalizacjaSelectDeleteView(FormView):  #skoro nie mam ustawionego delete.html to rowniez moge usunac?
    form_class = LokalizacjaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("lokalizacja_delete", pk=form.cleaned_data['lokalizacja'].id)


class LokalizacjaSelectUpdateView(FormView):
    form_class = LokalizacjaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("lokalizacja_update", pk=form.cleaned_data['lokalizacja'].id)


class LokalizacjaDeleteView(DeleteView):      #skoro nie mam ustawionego delete.html to rowniez moge usunac?
    template_name = 'lokalizacja_delete.html'
    model = Lokalizacja
    success_url = reverse_lazy("lokalizacja")