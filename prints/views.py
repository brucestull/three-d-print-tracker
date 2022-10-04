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

"""
from myapp.forms import ContactForm
from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
"""

class ModelPrintCreateView(LoginRequiredMixin, FormView):
    """
    Class-based view to create `ModelPrint` instances.
    """
    template_name = 'cb_model_print_create.html'
    form_class = CreateModelPrintForm
    
    def form_valid(self, form):
        print("'form_valid()' has been called")
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # print('type(self): ', type(self))
        # # type(self):  <class 'prints.views.ModelPrintCreateView'>
        # print('type(form): ', type(form))
        # # type(form):  <class 'prints.forms.CreateModelPrintForm'>

        print('form.cleaned_data: ', form.cleaned_data)
        # # form.cleaned_data:  {
        # #     'model_print_name': 'Totally New Print',
        # #     'filament_consumed': 2,
        # #     'filament_roll_chosen': <FilamentRoll: 28 - Manufacturer To Delete - Material To Delete>
        # # }

        return super().form_valid(form)

    # We want to give the template the current `FilamentRoll`s.
    def get_context_data(self,**kwargs):
        print("'get_context_data()' has been called")
        context = super().get_context_data(**kwargs)
        # Here we are adding more 'context' attributes.
        # print('context: ', context)
        # # context:  {
        # #     'form': <CreateModelPrintForm bound=False, valid=Unknown, fields=(model_print_name;filament_consumed;filament_roll_chosen)>,
        # #     'view': <prints.views.ModelPrintCreateView object at 0x000001DEDA8A2800>
        # # }

        context['filament_rolls'] = FilamentRoll.objects.all()
        # print('context: ', context)
        return context

    # Can I somehow pass the id of the newly created model `ModelPrint` to `get_success_url`?
    def get_success_url(self):
        print("'get_success_url()' has been called")
        # print('self: ', self)
        # # self:  <prints.views.ModelPrintCreateView object at 0x0000018AC1FF1FF0>

        return reverse(
            'prints:create_model_print',
        )


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

