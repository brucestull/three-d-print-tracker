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

from django.forms.models import modelform_factory

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
    # print(request)
    # print('dir(request): ', dir(request))
    # print('request.path: ', request.path)
    # print('request.headers: ', request.headers)
    print("request.headers['Origin']: ", request.headers['Origin'])
    print("request.headers['Referer']: ", request.headers['Referer'])

    the_origin = request.headers['Origin']
    the_referer = request.headers['Referer']
    the_url_we_want_to_go = the_referer.replace(the_origin, '')
    print('the_url_we_want_to_go: ', the_url_we_want_to_go)

    current_manufacturer = request.POST.get('manufacturer')
    current_material = request.POST.get('material')
    new_filament_roll = FilamentRoll.objects.create(
        manufacturer=current_manufacturer,
        material=current_material,
    )
    return HttpResponseRedirect(the_url_we_want_to_go)
    return HttpResponseRedirect(
        reverse('prints:model_print_function_view')
    )


class ModelPrintFormView(LoginRequiredMixin, FormView):
    """
    Class-based `FormView` to create `ModelPrint` instance.
    """
    form_class = CreateModelPrintForm
    template_name = 'model_print_create_fv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filament_roll_form = CreateFilamentRollForm()
        context['filament_roll_form'] = filament_roll_form

        filament_rolls = FilamentRoll.objects.all()
        context['filament_rolls_in_template'] = filament_rolls

        hard_coded_view_name = 'model_print_form_view'
        context['the_view_name'] = hard_coded_view_name
        print("'get_context_data()' has been called: ", context['the_view_name'])
        return context

    def get_success_url(self, model_print=None):
        the_url = reverse('prints:model_detail', kwargs={ 'pk': model_print.id})
        print("'get_success_url()' has been called: ", the_url)
        return the_url

    def form_valid(self, form):
        print("'form_valid() has been called:")

        current_filament_roll = form.cleaned_data['filament_roll_chosen']
        print('current_filament_roll: ', current_filament_roll)

        current_filament_consumed = form.cleaned_data['filament_consumed']
        print('current_filament_consumed: ', current_filament_consumed)

        current_model_print_name = form.cleaned_data['model_print_name']
        print('current_model_print_name: ', current_model_print_name)

        current_user = auth.get_user(self.request)
        print('current_user: ', current_user)

        new_filament_instance = FilamentInstance.objects.create(
            filament_consumed=current_filament_consumed,
            filament_roll=current_filament_roll,
        )

        new_model_print = ModelPrint.objects.create(
            name=current_model_print_name,
            creator=current_user,
            filament_instance=new_filament_instance,
        )
        print('new_model_print: ', new_model_print)

        the_success_url = self.get_success_url(new_model_print)

        return HttpResponseRedirect(the_success_url)


class ModelPrintCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based `CreateView` to create `ModelPrint` instance.

    This view doesn't function as needed yet. Haven't figured out how to programmatically create `FilamentInstance`.
    """
    model = ModelPrint
    template_name = 'model_print_create_cv.html'
    fields = [
        'name',
        # 'filament_instance',
    ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filament_roll_form = CreateFilamentRollForm()
        context['filament_roll_form'] = filament_roll_form

        filament_rolls = FilamentRoll.objects.all()
        context['filament_rolls_in_template'] = filament_rolls

        hard_coded_view_name = 'model_print_create_view'
        context['the_view_name'] = hard_coded_view_name

        print("'get_context_data()' has been called: ", context['the_view_name'])
        return context

    def get_success_url(self):
        new_model_print = self.object
        the_url = reverse('prints:model_detail', kwargs={ 'pk': new_model_print.id})
        print("'get_success_url()' has been called: ", the_url)
        return the_url

    def form_valid(self, form):
        print("'form_valid()' has been called:")
        the_request_post_keys = self.request.POST.keys()
        print('the_request_post_keys:', the_request_post_keys)

        filament_roll_id = self.request.POST.get('filament_roll')
        current_filament_roll = get_object_or_404(
            FilamentRoll,
            pk=filament_roll_id
        )
        current_filament_consumed = self.request.POST.get('filament_consumed')
        new_filament_instance = FilamentInstance.objects.create(
            filament_roll=current_filament_roll,
            filament_consumed=current_filament_consumed,
        )

        current_model_print_name = self.request.POST.get('name')
        current_user = auth.get_user(self.request)
        new_model_print = ModelPrint.objects.create(
            filament_instance=new_filament_instance,
            name=current_model_print_name,
            creator=current_user,
        )

        return HttpResponseRedirect(
            reverse('prints:model_detail', kwargs={ 'pk': new_model_print.id})
        )


def model_print_create_function(request):
    print("'model_print_create_function()' has been called:")
    
    if request.method == 'POST':
        filament_roll_id = request.POST.get('filament_roll_chosen')

        current_filament_roll = get_object_or_404(
            FilamentRoll,
            pk=filament_roll_id
        )
        current_filament_consumed = request.POST.get('filament_consumed')
        new_filament_instance = FilamentInstance.objects.create(
            filament_roll=current_filament_roll,
            filament_consumed=current_filament_consumed,
        )

        current_model_print_name = request.POST.get('model_print_name')
        current_user = auth.get_user(request)
        new_model_print = ModelPrint.objects.create(
            filament_instance=new_filament_instance,
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

        filament_rolls = FilamentRoll.objects.all()
        context['filament_rolls_in_template'] = filament_rolls

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

