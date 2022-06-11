from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from rejestr.forms.badania import BadaniaCreateForm
from rejestr.forms.badania import BadaniaSelect
from rejestr.models import Badania


# Create your views here.

class BadaniaCreateView(FormView):
    template_name = 'form.html'
    success_url = reverse_lazy("badania")
    form_class = BadaniaCreateForm

    def form_valid(self, form):
        result = super().form_valid(form)
        data = form.cleaned_data
        Badania.objects.create(
            nazwa=data['nazwa'],
        )
        return result


class BadaniaReadView(View):
    def get(self, request):

        return render(request, 'badania_read.html', context={'data': Badania.objects.all()})


class BadaniaUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy("badania")
    model = Badania
    form_class = BadaniaCreateForm

class BadaniaSelectDeleteView(FormView):
    form_class = BadaniaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("badania_delete", pk=form.cleaned_data['badania'].id)


class BadaniaSelectUpdateView(FormView):
    form_class = BadaniaSelect
    template_name = 'form.html'

    def form_valid(self, form):
        return redirect("badania_update", pk=form.cleaned_data['badania'].id)


class BadaniaDeleteView(DeleteView):
    template_name = 'badania_delete.html'
    model = Badania
    success_url = reverse_lazy("badania")