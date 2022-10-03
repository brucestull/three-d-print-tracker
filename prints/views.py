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

from prints.models import ModelPrint
from prints.models import FilamentRoll
from prints.models import FilamentInstance

from users.models import CustomUser

from django.contrib import auth


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

        # # print('POST - request: ', request)
        # print('POST - request.method: ', request.method)
        # # POST - request.method:  POST
        # print('request.POST.keys(): ', request.POST.keys())
        
        # print("reverse('prints:model_create_function_based'): ", reverse('prints:model_create_function_based'))
        # # reverse('prints:model_create_function_based'):  /prints/print/create-function-based/

        # ##### Do `POST` logic here.

        # #### 1. Maybe have drop-down for `FilamentRoll`. Temporarily use dummy roll:
            # #### Check request.POST.keys():
        # print('request.POST.keys(): ', request.POST.keys())
        # # request.POST.keys():  dict_keys(['csrfmiddlewaretoken', 'model-print-name', 'filament-roll-chosen', 'amount-of-filament-consumed'])

        # Where is this documented?
        # filament_roll_id = request.POST.get('filament-roll-chosen', None)
        
        filament_roll_id = request.POST.get('filament-roll-chosen')
        print(filament_roll_id)
        # current_filament_roll = FilamentRoll.objects.all()[0]
        current_filament_roll = get_object_or_404(FilamentRoll, pk=filament_roll_id)
        print("current_filament_roll: ", current_filament_roll)
        # # current_filament_roll:  6 : PLA+ : Very First Absolute Roll

        # #### 1. Input for `current_filament_consumed`:
        current_filament_consumed = request.POST.get('amount-of-filament-consumed')
        print("current_filament_consumed: ", current_filament_consumed)

        # #### 1. Get the `model-print-name` value:
        current_model_print_name = request.POST.get('model-print-name')
        print("current_model_print_name: ", current_model_print_name)
        # print('type(current_model_print_name): ', type(current_model_print_name))
        # # type(current_model_print_name):  <class 'str'>

        # #### 1. Create a `FilamentInstance` instance from `amount-of-filament-consumed` and `current_filament_roll`:
        current_filament_instance = FilamentInstance.objects.create(
            filament_consumed=current_filament_consumed,
            filament_roll=current_filament_roll
        )

        # #### 1. Get `current_user`:

        # print("type(current_user): ", type(current_user))
        # # type(current_user):  <class 'users.models.CustomUser'>
        # print("current_user: ", current_user)

        current_user = auth.get_user(request)


        # #### 1. Create a `ModelPrint` instance from `current_model_print_name`, `current_user`, and `current_filament_instance`:
        new_model_print = ModelPrint.objects.create(
            name=current_model_print_name,
            creator=current_user,
            filament_instance=current_filament_instance
        )
        print('new_model_print: ', new_model_print)

        return HttpResponseRedirect(reverse('prints:model_create_function_based'))


    elif request.method == 'GET':

        # print('GET - request: ', request)
        # # GET - request:  <WSGIRequest: GET '/prints/print/create-function-based/'>
        # print('GET - request.method: ', request.method)
        # # GET - request.method:  GET

        # ##### Do `GET` logic here.
        # #### 1. Get `FilamentRoll` instance(S) information so we can display in a drop-down:
        filament_rolls = FilamentRoll.objects.all()

        # #### 1. Add `filament_rolls` to `context`:
        context = {
            'filament_rolls_in_template': filament_rolls
        }
        # #### 1. Display `FilamenRoll` instance information in a drop-down on template.

        return render(request, 'model_print_create_function_based.html', context)


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

