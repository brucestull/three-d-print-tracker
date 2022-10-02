from django.db import models
from django.urls import reverse

from print_tracker.settings.common import AUTH_USER_MODEL


class Manufacturer(models.Model):
    """
    Model for the `prints.manufacturer` of a `prints.filamentinstance` object.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'


class FilamentRoll(models.Model):
    """
    Model for the `prints.filamentroll` used in each `prints.filamentinstance` instance.
    Need to figure out a way to make a unique 'id'.
    Might use 'choices', in future, for 'material'.
    """
    material = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.material}'


def get_or_create_a_deleted_filament_roll():
    """
    Gets an existing `prints.filamentroll` object or creates a new `prints.filamentroll` object which has `material` attribute of `deleted`. The [0] gets the first element of the QuerySet.
    """
    return FilamentRoll.objects.get_or_create(material='deleted')[0]


class FilamentInstance(models.Model):
    """
    Model for the `prints.filamentinstance` used in `prints.modelprint`.
    """
    material = models.CharField(max_length=255)
    filament_roll = models.ForeignKey(
        FilamentRoll,
        on_delete=models.SET(
            get_or_create_a_deleted_filament_roll
        ),
    )

    def __str__(self):
        return f'{self.id} : {self.filament_roll}'


def get_or_create_a_deleted_filament_instance():
    """
    Gets an existing `prints.filamentinstance` object or creates a new `prints.filamentinstance` object which has `filament_roll` attribute of `deleted`. The [0] gets the first element of the QuerySet.
    """
    return FilamentInstance.objects.get_or_create(material='deleted')[0]


class ModelPrint(models.Model):
    """
    Model for each instance of a printed 3D object.
    """
    name = models.CharField("Name of 3D Print Model", max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='prints',
        on_delete=models.CASCADE,
    )
    filament_instance = models.ForeignKey(
        FilamentInstance,
        related_name='prints',
        on_delete=models.SET(
            get_or_create_a_deleted_filament_instance
        ),
    )

    def __str__(self):
        return (
            f'{self.id} : '
            f'{self.name} : '
            f'{self.creator.username} : '
            f'{self.filament_instance.filament_roll if self.filament_instance else "No filament_instance provided"}'
        )
    
    def get_absolute_url(self):
        return reverse('prints:model_detail', args=(self.pk,))
