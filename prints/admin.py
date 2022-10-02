from django.contrib import admin

from .models import ModelPrint
from .models import FilamentInstance
from .models import Manufacturer


admin.site.register(ModelPrint)
admin.site.register(FilamentInstance)
admin.site.register(Manufacturer)


