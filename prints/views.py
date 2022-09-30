from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import ModelPrint


class ModelPrintListView(ListView):
    """
    Class-based view, which inherits from `django.views.generic.ListView`, to provide list view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name = 'model_print_list.html'


class ModelPrintDetailView(DetailView):
    model = ModelPrint
    template_name ='model_print_detail.html'


class ModelPrintCreateView(CreateView):
    model = ModelPrint
    template_name ='model_print_create.html'
    fields = ['name', 'creator', 'filament']


