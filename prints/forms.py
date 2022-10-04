from django import forms

from .models import FilamentRoll


class CreateModelPrintForm(forms.Form):
    model_print_name = forms.CharField(
        label='Model Print Name',
        max_length=255,
    )
    filament_consumed = forms.CharField(
        label="Filament Consumed",
        help_text='Units of grams (g)',
        max_length=100,
        widget=forms.NumberInput(),
    )
    filament_roll_chosen = forms.ModelChoiceField(
        label='Filament Roll Chosen',
        help_text='Available Rolls',
        queryset=FilamentRoll.objects.all(),
    )


class CreateFilamentRollForm(forms.ModelForm):
    class Meta:
        model = FilamentRoll
        fields = [
            'material',
            'manufacturer'
        ]