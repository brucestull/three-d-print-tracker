from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic import ListView
from django.views.generic import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin

from django.contrib import auth

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import get_object_or_404


from prints.models import ModelPrint
from prints.models import FilamentRoll
from prints.models import FilamentInstance

from .forms import CreateModelPrintForm
from .forms import CreateFilamentRollForm


class ModelPrintListView(ListView):
    """
    Class-based view, which inherits from `django.views.generic.list.ListView`, to provide list view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name = 'model_print_list.html'


class ModelPrintDetailView(DetailView):
    """
    Class-based view, which inherits from `django.views.generic.detail.DetailView`, to provide detail view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name ='model_print_detail.html'


def create_filament_roll(request):
    current_manufacturer = request.POST.get('manufacturer')
    current_material = request.POST.get('material')
    new_filament_roll = FilamentRoll.objects.create(
        manufacturer=current_manufacturer,
        material=current_material,
    )
    return HttpResponseRedirect(
        reverse('prints:create_model_print')
    )



class ModelPrintCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view to create `ModelPrint` instances.
    """
    model = ModelPrint
    template_name = 'cb_model_print_create.html'
    fields = [
        'name',
        'filament_instance',
    ]

    def form_valid(self, form):
        print("'form_valid()' has been called:")
        # print('self: ', self)
        # # self:  <prints.views.ModelPrintCreateView object at 0x000002B6B3A81780>
        # print('form: ', form)
        # # An HTML form.
        form.instance.creator = self.request.user
        return super(ModelPrintCreateView, self).form_valid(form)
    
    def get_success_url(self):
        print("'get_success_url()' has been called:")
        # print('type(self.object): ', type(self.object))
        # # type(self.object):  <class 'prints.models.ModelPrint'>
        print('self.object.name: ', self.object.name)
        print('self.object.id: ', self.object.id)
        new_model_print = self.object
        return reverse('prints:model_detail', kwargs={ 'pk': new_model_print.id})


def model_print_create_function(request):
    
    if request.method == 'POST':
        filament_roll_id = request.POST.get('filament_roll_chosen')

        # Create a current `FilamentInstance` from user input:
        current_filament_roll = get_object_or_404(
            FilamentRoll,
            pk=filament_roll_id
        )
        current_filament_consumed = request.POST.get('filament_consumed')
        current_filament_instance = FilamentInstance.objects.create(
            filament_roll=current_filament_roll,
            filament_consumed=current_filament_consumed,
        )

        # Create a new `ModelPrint` from user input and `auth.get_user()`:
        current_model_print_name = request.POST.get('model_print_name')
        current_user = auth.get_user(request)
        new_model_print = ModelPrint.objects.create(
            filament_instance=current_filament_instance,
            name=current_model_print_name,
            creator=current_user,
        )
        return HttpResponseRedirect(
            reverse('prints:model_detail', kwargs={ 'pk': new_model_print.id})
        )

    elif request.method == 'GET':
        create_model_print_form = CreateModelPrintForm()
        create_filament_roll_form = CreateFilamentRollForm()
        context = {
            'model_print_form': create_model_print_form,
            'filament_roll_form': create_filament_roll_form,
        }
        return render(
            request,
            'model_print_create.html',
            context
        )


class ModelPrintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Class-based view, which inherits from `LoginRequiredMixin`, `UserPassesTestMixin`, and `django.views.generic.UpdateView`. Allows users to update their own `ModelPrint` instances.
    """
    model = ModelPrint
    template_name ='model_print_update.html'
    fields = ['name', 'filament_instance']

    def test_func(self):
        """
        Returns `True` if `self.request.user` is `model_print.creator`. In other words, returns `True` if the user requesting to update the `ModelPrint` is the user who is associated with the `ModelPrint`.
        """
        model_print = self.get_object()
        return self.request.user == model_print.creator


class ModelPrintDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class-based view, which inherits from `django.contrib.auth.mixins.LoginRequiredMixin`, `django.contrib.auth.mixins.UserPassesTestMixin`, and `django.views.generic.edit.DeleteView`. Allows users to delete their own `ModelPrint` instances.
    """
    model = ModelPrint
    template_name ='model_print_delete.html'
    success_url = reverse_lazy('prints:home')

    def test_func(self):
        """
        Returns `True` if `self.request.user` is `model_print.creator`. In other words, returns `True` if the user requesting to delete the `ModelPrint` is the user who is associated with the `ModelPrint`.
        """
        model_print = self.get_object()
        return self.request.user == model_print.creator

