from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from rejestr.forms.dieta import DietaCreateForm
from rejestr.forms.dieta import DietaSelect
from rejestr.models import Dieta


# Create your views here.

class DietaCreateView(FormView):
    template_name = 'form.html'
    success_url = reverse_lazy("dieta")
    form_class = DietaCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        Dieta.objects.create(
            nazwa=data['nazwa'],
        )
        return result


class DietaReadView(View):
    def get(self, request):

        return render(request, 'dieta_read.html', context={'data': Dieta.objects.all()})


class DietaUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy("dieta")
    model = Dieta
    form_class = DietaCreateForm

class DietaSelectDeleteView(FormView):
    form_class = DietaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("dieta_delete", pk=form.cleaned_data['dieta'].id)


class DietaSelectUpdateView(FormView):
    form_class = DietaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("dieta_update", pk=form.cleaned_data['dieta'].id)


class DietaDeleteView(DeleteView):
    template_name = 'dieta_delete.html'
    model = Dieta
    success_url = reverse_lazy("dieta")