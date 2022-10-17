from django.contrib import admin

from .models import ModelPrint
from .models import FilamentInstance
from .models import FilamentRoll
from .models import Manufacturer
from .models import FilamentMaterial


admin.site.register(ModelPrint)
admin.site.register(FilamentInstance)
admin.site.register(FilamentRoll)
admin.site.register(FilamentMaterial)
admin.site.register(Manufacturer)


