from django.contrib import admin

from .models import ModelPrint
from .models import Filament
from .models import Manufacturer


admin.site.register(ModelPrint)
admin.site.register(Filament)
admin.site.register(Manufacturer)


