from django import forms

from .models import FilamentRoll


class CreateModelPrintForm(forms.Form):
    model_print_name = forms.CharField(
        label='Model Print Name',
        max_length=255,
    )
    filament_consumed = forms.IntegerField(
        label="Filament Consumed",
        help_text='Units of grams (g)',
        min_value=0,
    )
    filament_roll_chosen = forms.ModelChoiceField(
        label='Filament Roll Chosen',
        help_text='Available Rolls',
        queryset=FilamentRoll.objects.all(),
    )


class CreateFilamentRollForm(forms.Form):
    manufacturer = forms.CharField(
        label='Manufacturer',
        max_length=255,
    )
    material = forms.CharField(
        label='Material',
        max_length=255,
    )
