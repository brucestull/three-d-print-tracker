from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.urls import reverse

from django.contrib import auth

from prints.models import ModelPrint
from prints.models import FilamentRoll
from prints.models import FilamentInstance

from .forms import CreateModelPrintForm

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


class ModelPrintCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view, which inherits from `django.views.generic.edit.CreateView` and ``, to provide a `CreateView` for `ModelPrint`.
    """
    model = ModelPrint
    template_name ='model_print_create.html'
    fields = ['name', 'filament_instance']

    def form_valid(self, form):
        """
        Set `form.instance.creator` as `self.request.user` when valid form data is provided.
        """
        form.instance.creator = self.request.user
        return super().form_valid(form)


def create_model_print(request):
    
    if request.method == 'POST':
        filament_roll_id = request.POST.get('filament_roll_chosen')
        current_filament_roll = get_object_or_404(
            FilamentRoll,
            pk=filament_roll_id
        )
        current_filament_consumed = request.POST.get('filament_consumed')
        current_model_print_name = request.POST.get('model_print_name')
        current_filament_instance = FilamentInstance.objects.create(
            filament_consumed=current_filament_consumed,
            filament_roll=current_filament_roll
        )
        current_user = auth.get_user(request)
        new_model_print = ModelPrint.objects.create(
            name=current_model_print_name,
            creator=current_user,
            filament_instance=current_filament_instance
        )
        return HttpResponseRedirect(
            reverse('prints:model_create_function_based')
        )

    elif request.method == 'GET':
        create_model_print_form = CreateModelPrintForm()
        context = {
            'form': create_model_print_form,
        }
        return render(
            request,
            'model_print_create_function_based.html',
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

