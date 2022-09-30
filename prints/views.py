from django.views.generic import ListView

from .models import ModelPrint


class ModelPrintListView(ListView):
    """
    Class-based view, which inherits from `django.views.generic.ListView`, to provide list view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name = 'model_print_list.html'
