from django.db import models
from django.urls import reverse

from print_tracker.settings.common import AUTH_USER_MODEL


class Manufacturer(models.Model):
    """
    Model for the `prints.manufacturer` of a `prints.filamentinstance` object.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FilamentRoll(models.Model):
    """
    Model for the `prints.filamentroll` used in each `prints.filamentinstance` instance.
    Need to figure out a way to make a unique 'id'.
    Might use 'choices', in future, for 'material'.
    """
    manufacturer = models.CharField(max_length=255)
    material = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.manufacturer} - {self.material}'


class FilamentInstance(models.Model):
    """
    Model for the `prints.filamentinstance` used in `prints.modelprint`.
    """
    filament_consumed = models.IntegerField(default=0)
    filament_roll = models.ForeignKey(
        FilamentRoll,
        # `PROTECT` prevents deletion of `FilamentRoll` instance if it is associated with a `FilamentInstance` instance.
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{self.filament_consumed} - {self.filament_roll}'


class ModelPrint(models.Model):
    """
    Model for each instance of a printed 3D object.
    """
    name = models.CharField("Name of 3D Print Model", max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='prints',
        # `CASCADE` deletes `ModelPrint` on deletion of associated `CustomUser` instance.
        on_delete=models.CASCADE,
    )
    filament_instance = models.OneToOneField(
        FilamentInstance,
        related_name='print',
        # `PROTECT` prevents deletion of `FilamentInstance` instance if it is associated with a `ModelPrint` instance.
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return (
            f'{self.id} : '
            f'{self.name} : '
            f'{self.creator.username} : '
            f'{self.filament_instance.filament_consumed if self.filament_instance else "No FilamentInstance provided"} grams of '
            f'"{self.filament_instance.filament_roll if self.filament_instance else "No FilamentInstance provided"}"'
        )
    
    def get_absolute_url(self):
        return reverse('prints:model_detail', args=(self.pk,))
