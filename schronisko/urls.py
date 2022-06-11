"""schronisko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from rejestr.views.pies import PiesCreateView
from rejestr.views.pies import PiesReadView
from rejestr.views.pies import PiesSelectUpdateView
from rejestr.views.pies import PiesUpdateView
from rejestr.views.pies import PiesSelectDeleteView
from rejestr.views.pies import PiesDeleteView

from rejestr.views.badania import BadaniaCreateView
from rejestr.views.badania import BadaniaReadView
from rejestr.views.badania import BadaniaSelectUpdateView
from rejestr.views.badania import BadaniaUpdateView
from rejestr.views.badania import BadaniaSelectDeleteView
from rejestr.views.badania import BadaniaDeleteView

from rejestr.views.pies_badania import Pies_badaniaCreateView
from rejestr.views.pies_badania import Pies_badaniaReadView
from rejestr.views.pies_badania import Pies_badaniaSelectUpdateView
from rejestr.views.pies_badania import Pies_badaniaUpdateView
from rejestr.views.pies_badania import Pies_badaniaSelectDeleteView
from rejestr.views.pies_badania import Pies_badaniaDeleteView

from rejestr.views.dieta import DietaCreateView
from rejestr.views.dieta import DietaReadView
from rejestr.views.dieta import DietaSelectUpdateView
from rejestr.views.dieta import DietaUpdateView
from rejestr.views.dieta import DietaSelectDeleteView
from rejestr.views.dieta import DietaDeleteView

from rejestr.views.leczenie import LeczenieCreateView
from rejestr.views.leczenie import LeczenieReadView
from rejestr.views.leczenie import LeczenieSelectUpdateView
from rejestr.views.leczenie import LeczenieUpdateView
from rejestr.views.leczenie import LeczenieSelectDeleteView
from rejestr.views.leczenie import LeczenieDeleteView

from rejestr.views.lokalizacja import LokalizacjaCreateView
from rejestr.views.lokalizacja import LokalizacjaReadView
from rejestr.views.lokalizacja import LokalizacjaSelectUpdateView
from rejestr.views.lokalizacja import LokalizacjaUpdateView
from rejestr.views.lokalizacja import LokalizacjaSelectDeleteView
from rejestr.views.lokalizacja import LokalizacjaDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pies/create', PiesCreateView.as_view()),
    path('pies/read', PiesReadView.as_view(), name="pies"),
    path('pies/update', PiesSelectUpdateView.as_view()),
    path('pies/update/<pk>', PiesUpdateView.as_view(), name="pies_update"),
    path('pies/delete', PiesSelectDeleteView.as_view()),
    path('pies/delete/<pk>', PiesDeleteView.as_view(), name="pies_delete"),
    path('badania/create', BadaniaCreateView.as_view()),
    path('badania/read', BadaniaReadView.as_view(), name="pies"),
    path('badania/update', BadaniaSelectUpdateView.as_view()),
    path('badania/update/<pk>', BadaniaUpdateView.as_view(), name="pies_update"),
    path('badania/delete', BadaniaSelectDeleteView.as_view()),
    path('badania/delete/<pk>', BadaniaDeleteView.as_view(), name="pies_delete"),
    path('pies_badania/create',Pies_badaniaCreateView.as_view()),
    path('pies_badania/read', Pies_badaniaReadView.as_view(), name="pies"),
    path('pies_badania/update', Pies_badaniaSelectUpdateView.as_view()),
    path('pies_badania/update/<pk>', Pies_badaniaUpdateView.as_view(), name="pies_update"),
    path('pies_badania/delete', Pies_badaniaSelectDeleteView.as_view()),
    path('pies_badania/delete/<pk>', Pies_badaniaDeleteView.as_view(), name="pies_delete"),
    path('dieta/create', DietaCreateView.as_view()),
    path('dieta/read', DietaReadView.as_view(), name="pies"),
    path('dieta/update', DietaSelectUpdateView.as_view()),
    path('dieta/update/<pk>', DietaUpdateView.as_view(), name="pies_update"),
    path('dieta/delete', DietaSelectDeleteView.as_view()),
    path('dieta/delete/<pk>', DietaDeleteView.as_view(), name="pies_delete"),
    path('leczenie/create', LeczenieCreateView.as_view()),
    path('leczenie/read', LeczenieReadView.as_view(), name="pies"),
    path('leczenie/update', LeczenieSelectUpdateView.as_view()),
    path('leczenie/update/<pk>', LeczenieUpdateView.as_view(), name="pies_update"),
    path('leczenie/delete', LeczenieSelectDeleteView.as_view()),
    path('leczenie/delete/<pk>', LeczenieDeleteView.as_view(), name="pies_delete"),
    path('lokalizacja/create', LokalizacjaCreateView.as_view()),
    path('lokalizacja/read', LokalizacjaReadView.as_view(), name="pies"),
    path('lokalizacja/update', LokalizacjaSelectUpdateView.as_view()),
    path('lokalizacja/update/<pk>', LokalizacjaUpdateView.as_view(), name="pies_update"),
    path('lokalizacja/delete', LokalizacjaSelectDeleteView.as_view()),
    path('lokalizacja/delete/<pk>', LokalizacjaDeleteView.as_view(), name="pies_delete")
]
