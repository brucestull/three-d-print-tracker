from django import forms

from .models import FilamentRoll

class CreateModelPrintForm(forms.Form):
    model_print_name = forms.CharField(max_length=255)
    filament_consumed = forms.CharField(
        widget=forms.NumberInput(),
        max_length=100
    )
    filament_roll_chosen = forms.ModelChoiceField(
        queryset=FilamentRoll.objects.all()
    )