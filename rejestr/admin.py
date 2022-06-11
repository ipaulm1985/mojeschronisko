from django.contrib import admin

# Register your models here.
from rejestr.models import Pies
from rejestr.models import Badania
from rejestr.models import Pies_badania
from rejestr.models import Leczenie
from rejestr.models import Pies_leczenie
from rejestr.models import Dieta
from rejestr.models import Pies_dieta
from rejestr.models import Lokalizacja

admin.site.register(Pies)
admin.site.register(Badania)
admin.site.register(Pies_badania)
admin.site.register(Leczenie)
admin.site.register(Pies_leczenie)
admin.site.register(Dieta)
admin.site.register(Pies_dieta)
admin.site.register(Lokalizacja)
