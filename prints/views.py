from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from prints.models import ModelPrint


class ModelPrintListView(ListView):
    """
    Class-based view, which inherits from `django.views.generic.ListView`, to provide list view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name = 'model_print_list.html'


class ModelPrintDetailView(DetailView):
    """
    Class-based view, which inherits from `django.views.generic.DetailView`, to provide detail view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name ='model_print_detail.html'


class ModelPrintCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view, which inherits from `django.views.generic.CreateView` and ``, to provide a `CreateView` for `ModelPrint`.
    """
    model = ModelPrint
    template_name ='model_print_create.html'
    fields = ['name', 'filament']

    def form_valid(self, form):
        """
        Set `form.instance.creator` as `self.request.user` when valid form data is provided.
        """
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ModelPrintUpdateView(UpdateView):
    model = ModelPrint
    template_name ='model_print_update.html'
    fields = ['name', 'creator', 'filament']


class ModelPrintDeleteView(DeleteView):
    model = ModelPrint
    template_name ='model_print_delete.html'
    success_url = reverse_lazy('prints:home')


