# Create `FilamentRoll` `CreateView`

## Resources:

## Process:

### Using `forms.ModelForm`:

1. Add route for `FilamentRollCreateView` to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/create-filament-roll/', views.FilamentRollCreateView.as_view(), name='create_filament_roll'),
        #...
    ]
    ```

1. Add `forms.ModelForm`-based `CreateFilamentRollForm` in [`prints/forms.py`](../prints/forms.py):
    ```
    class CreateFilamentRollForm(forms.ModelForm):
        class Meta:
            model = FilamentRoll
            fields = [
                'material',
                'manufacturer'
            ]
    ```

1. Add `FilamentRollCreateView` in [`prints/views.py`](../prints/views.py):
    ```
    class FilamentRollCreateView(LoginRequiredMixin, CreateView):
        """
        Class-based view, which inherits from `django.views.generic.edit.CreateView` and `django.contrib.auth.mixins.LoginRequiredMixin`, to provide a `CreateView` for `FilamentRoll`.
        """
        # TODO: Maybe use `context` here so I don't have to route back to `create_model_print`, but, I would need to get 'rolls' in both cases.
        model = FilamentRoll
        fields = [
            'manufacturer',
            'material',
        ]

        def get_success_url(self):
            return reverse('prints:create_model_print')
    ```

1. Repository state:
    * [Commit `0523aefa56d51ff236fc395a59a82531f0664118`](https://github.com/brucestull/see-3d/tree/0523aefa56d51ff236fc395a59a82531f0664118)

### Using `forms.Form`:

1. Add `forms.Form`-based `CreateFilamentRollForm` to [`prints/forms.py`](../prints/forms.py):
    ```
    class CreateFilamentRollForm(forms.Form):
        manufacturer = forms.CharField(
            label='Manufacturer',
            max_length=255,
        )
        material = forms.CharField(
            label='Material',
            max_length=255,
        )
    ```

1. Add `create_filament_roll` to [`prints/views.py`](../prints/views.py):
    ```
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
    ```

1. Add route `print/create-model-print/` to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/create-filament-roll/', views.create_filament_roll, name='create_filament_roll'),
        #...
    ]
    ```

1. Test new views:
    * `python .\manage.py runserver`
    * http://localhost:8000/prints/print/create-model-print/


1. Proceed to []()

## Repository Links:
* Back to [Convert `ModelPrint` `CreateView` to Function-Based View](./15_convert_create_view_to_function_based.md)
* [README.md](../README.md)