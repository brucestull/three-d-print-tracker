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
    model = ModelPrint
    template_name ='model_print_detail.html'


class ModelPrintCreateView(LoginRequiredMixin, CreateView):
    model = ModelPrint
    template_name ='model_print_create.html'
    fields = ['name', 'filament']

    def form_valid(self, form):

        # print('self: ', self)
        # <prints.views.ModelPrintCreateView object at 0x00000242A0E4CDC0>
        # print('form: ', form)
        # Some HTML form-looking thing.

        # print('self.request: ', self.request)
        # self.request:  <WSGIRequest: POST '/prints/print/create/'>

        # print('self.request.keys(): ', self.request.keys())
        # Breaks, no such 'keys()' thing.

        # print('self.request.POST: ', self.request.POST)
        """
        self.request.POST:  <QueryDict: {
            'csrfmiddlewaretoken': ['IkmVDHQMZhPYF4sH69lqTsca58DZqMBvFX9L856UOfCAnkWoi1uDt9QJPD3C2Zu0'],
            'name': ['A Model Print Name'],
            'creator': ['1'],
            'filament': ['10']
        }>
        """

        # print('self.request.user: ', self.request.user)
        # self.request.user:  admin
        # print('type(self.request.user): ', type(self.request.user))
        # type(self.request.user):  <class 'django.utils.functional.SimpleLazyObject'>

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


