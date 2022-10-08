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
    Need to figure out a way to make a unique identifier other than `id`.
    Something more than just one or two characters.
    Might use 'choices', in future, for 'material'.
    """
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name='rolls',
        # `PROTECT` prevents deletion of `Manufacturer` instance if it is associated with a `FilamentRoll` instance.
        on_delete=models.PROTECT,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='rolls',
        # `CASCADE` allows deletion of `AUTH_USER_MODEL` instance and also does a cascading deletion of `FilamentRoll` instance.
        # `PROTECT` prevents deletion of `AUTH_USER_MODEL` instance if it is associated with a `FilamentRoll` instance.
        # `SET_NULL` Set the ForeignKey null; this is only possible if null is True..
        on_delete=models.SET_NULL,
        null=True,
    )
    material = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.material} - {self.manufacturer.name} - #{self.id}'

    def get_absolute_url(self):
        return reverse('prints:roll_detail', args=(self.pk,))


class FilamentInstance(models.Model):
    """
    Model for the `prints.filamentinstance` used in `prints.modelprint`.
    """
    filament_consumed = models.IntegerField(default=0)
    filament_roll = models.ForeignKey(
        FilamentRoll,
        related_name='instances',
        # `PROTECT` prevents deletion of `FilamentRoll` instance if it is associated with a `FilamentInstance` instance.
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{self.filament_consumed}g'
        return f'{self.filament_consumed}g of {self.filament_roll}'


class ModelPrint(models.Model):
    """
    Model for each instance of a printed 3D object.
    """
    name = models.CharField("Name of 3D Print Model", max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='prints',
        # `CASCADE` allows deletion of `AUTH_USER_MODEL` instance and also does a cascading deletion of `ModelPrint`.
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
            self.name

            # f'{self.id} : '
            # f'{self.name} : '
            # f'{self.creator.username} : '
            # f'{self.filament_instance.filament_consumed if self.filament_instance else "No FilamentInstance provided"} grams of '
            # f'"{self.filament_instance.filament_roll if self.filament_instance else "No FilamentInstance provided"}"'
        )
    
    def get_absolute_url(self):
        return reverse('prints:model_detail', args=(self.pk,))
