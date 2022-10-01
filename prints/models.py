from django.db import models
from django.urls import reverse

from print_tracker.settings.common import AUTH_USER_MODEL


class Manufacturer(models.Model):
    """
    Model for the `Manufacturer` of a `Filament` object.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'


def get_or_create_a_deleted_manufacturer():
    """
    Gets an existing `Manufacturer` object or creates a new `Manufacturer` object which has `name` attribute of `deleted`. The [0] gets the first element of the QuerySet.
    """
    return Manufacturer.objects.get_or_create(name='deleted')[0]


class FilamentRoll(models.Model):
    """
    Model for the `Filament` used in `ModelPrint`.
    """
    material = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name='manufacturers',
        on_delete=models.SET(
            get_or_create_a_deleted_manufacturer
        )
    )

    def __str__(self):
        return f'{self.id} : {self.material} : {self.manufacturer.name}'


def get_or_create_a_deleted_filament_roll():
    """
    Gets an existing `FilamentRoll` object or creates a new `FilamentRoll` object which has `manufacturer` attribute of `deleted`. The [0] gets the first element of the QuerySet.
    """
    return FilamentRoll.objects.get_or_create(manufacturer='deleted')[0]

class FilamentInstance(models.Model):
    """
    Instances of `Filament`. The actual filament consumed by a model print.
    """
    filament_used = models.FloatField(default=0)
    filament_roll = models.ForeignKey(
        FilamentRoll,
        related_name='rolls',
        on_delete=models.SET(
            get_or_create_a_deleted_filament_roll
        )
    )


def get_or_create_a_deleted_filament_instance():
    """
    Gets an existing `FilamentInstance` object or creates a new `FilamentInstance` object which has `filament_roll` attribute of `deleted`. The [0] gets the first element of the QuerySet.
    """
    return FilamentInstance.objects.get_or_create(filament_roll='deleted')[0]


class ModelPrint(models.Model):
    """
    Model for each instance of a printed 3D object.
    """
    name = models.CharField("Name of 3D Print Model", max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='prints',
        on_delete=models.CASCADE
    )
    filament_instance = models.ForeignKey(
        FilamentInstance,
        related_name='prints',
        on_delete=models.SET(
            get_or_create_a_deleted_filament_instance
        )
    )

    def __str__(self):
        return (
            f'{self.name} : '
            f'{self.creator.username} : '
            f'{self.filament_instance.filament_roll.material if self.filament_instance.filament_roll else "No filament provided"} : '
            f'{self.id}'
        )
    
    def get_absolute_url(self):
        return reverse('prints:model_detail', args=(self.pk,))
