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

from django.forms.models import modelform_factory
import pprint

from prints.models import Manufacturer
from prints.models import FilamentMaterial
from prints.models import FilamentRoll
from prints.models import FilamentInstance
from prints.models import ModelPrint

from .forms import CreateModelPrintForm
from .forms import CreateFilamentRollForm


#================================================================
## `Manufacturer` Views:
class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    template_name = 'manufacturers/manufacturer_list.html'


class ManufacturerDetailView(LoginRequiredMixin, DetailView):
    model = Manufacturer
    template_name ='manufacturers/manufacturer_detail.html'


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    template_name = 'manufacturers/manufacturer_create.html'
    fields = [
        'name',
    ]


class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    template_name = 'manufacturers/manufacturer_edit.html'
    fields = [
        'name',
    ]


class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manufacturer
    template_name = 'manufacturers/manufacturer_delete.html'
    success_url = reverse_lazy('prints:manufacturers')
#================================================================


#================================================================
## `FilamentRoll` Views:
class FilamentRollListView(LoginRequiredMixin, ListView):
    model = FilamentRoll
    template_name = 'filament_rolls/filament_roll_list.html'


class FilamentRollDetailView(LoginRequiredMixin, DetailView):
    model = FilamentRoll
    template_name = 'filament_rolls/filament_roll_detail.html'


class FilamentRollCreateView(LoginRequiredMixin, CreateView):
    model = FilamentRoll
    template_name = 'filament_rolls/filament_roll_create.html'
    fields = [
        'manufacturer',
        'material',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filament_materials'] = FilamentMaterial.objects.all()
        return context

    def form_valid(self, form):
        print('self.request.user: ', self.request.user)
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FilamentRollUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FilamentRoll
    template_name = 'filament_rolls/filament_roll_edit.html'
    fields = [
       'manufacturer',
       'material',
    ]

    def test_func(self):
        roll = self.get_object()
        print('roll: ', roll)
        return self.request.user == roll.owner


class FilamentRollDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FilamentRoll
    template_name ='filament_rolls/filament_roll_delete.html'
    success_url = reverse_lazy('prints:rolls')

    def test_func(self):
        roll = self.get_object()
        print('roll: ', roll)
        return self.request.user == roll.owner
#================================================================


#================================================================
## `FilamentInstance` Views:
class FilamentInstanceListView(LoginRequiredMixin, ListView):
    model = FilamentInstance
    template_name = 'filament_instances/filament_instance_list.html'


class FilamentInstanceDetailView(LoginRequiredMixin, DetailView):
    model = FilamentInstance
    template_name = 'filament_instances/filament_instance_detail.html'


class FilamentInstanceCreateView(LoginRequiredMixin, CreateView):
    model = FilamentInstance
    template_name = 'filament_instances/filament_instance_create.html'
    fields = [
        'grams_filament_consumed',
        'filament_roll',
    ]


class FilamentInstanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FilamentInstance
    template_name = 'filament_instances/filament_instance_edit.html'
    fields = [
        'grams_filament_consumed',
        'filament_roll',
    ]

    def test_func(self):
        filament_instance = self.get_object()
        print('filament_instance: ', filament_instance)
        return self.request.user == filament_instance.filament_roll.owner


class FilamentInstanceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FilamentInstance
    template_name = 'filament_instances/filament_instance_delete.html'
    success_url = reverse_lazy('prints:filament_instances')

    def test_func(self):
        filament_instance = self.get_object()
        print('filament_instance: ', filament_instance)
        print(f"FilamentInstance deletion possible: {not hasattr(filament_instance, 'print')}")
        return (
            # User is `FilamentRoll` `owner`:
            self.request.user == filament_instance.filament_roll.owner
            and
            # `FilamentInstance` has no associated `ModelPrint`s:
            not hasattr(filament_instance, 'print')
        )

#================================================================


#================================================================
## `ModelPrint` Views:
class ModelPrintListView(LoginRequiredMixin, ListView):
    """
    Class-based view, which inherits from `django.views.generic.list.ListView`, to provide list view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name = 'prints/model_print_list.html'


class ModelPrintDetailView(LoginRequiredMixin, DetailView):
    """
    Class-based view, which inherits from `django.views.generic.detail.DetailView`, to provide detail view of model `ModelPrint`.
    """
    model = ModelPrint
    template_name = 'prints/model_print_detail.html'


def new_model_print(request):
    print("\n\n'new_model_print()' has been called:")
    
    if request.method == 'POST':
        filament_roll_id = request.POST.get('filament_roll_chosen')

        current_filament_roll = get_object_or_404(
            FilamentRoll,
            pk=filament_roll_id
        )
        current_filament_consumed = request.POST.get('grams_filament_consumed')
        new_filament_instance = FilamentInstance.objects.create(
            filament_roll=current_filament_roll,
            grams_filament_consumed=current_filament_consumed,
        )

        current_model_print_name = request.POST.get('model_print_name')
        current_user = auth.get_user(request)
        new_model_print = ModelPrint.objects.create(
            filament_instance=new_filament_instance,
            name=current_model_print_name,
            creator=current_user,
        )
        print('new_model_print: ', new_model_print)
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

        filament_rolls = FilamentRoll.objects.all()
        context['filament_rolls_in_template'] = filament_rolls

        print('context: ')
        pprint.pprint(context)
        return render(
            request,
            'prints/model_print_create.html',
            context
        )


class ModelPrintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Class-based view, which inherits from `LoginRequiredMixin`, `UserPassesTestMixin`, and `django.views.generic.UpdateView`. Allows users to update their own `ModelPrint` instances.
    """
    model = ModelPrint
    template_name ='prints/model_print_edit.html'
    fields = ['name']

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
    template_name ='prints/model_print_delete.html'
    success_url = reverse_lazy('prints:models')

    def test_func(self):
        """
        Returns `True` if `self.request.user` is `model_print.creator`. In other words, returns `True` if the user requesting to delete the `ModelPrint` is the user who is associated with the `ModelPrint`.
        """
        model_print = self.get_object()
        return self.request.user == model_print.creator
#================================================================


#================================================================
## User Prints Profile View
class UserPrintsProfileView(LoginRequiredMixin, ListView):
    template_name = 'users_prints/user_print_profile.html'

    def get_context_data(self,**kwargs):
        # Get the Django-provided context dictionary.
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        # Add `current_user` to the context dictionary.
        context['current_user'] = current_user
        return context

    def get_queryset(self):
        """
        Get only the `ModelPrint` instances which have a 'creator' of
        the current logged in 'user' (The 'user' who made the 'request').
        """
        return ModelPrint.objects.filter(creator=self.request.user)
#================================================================

