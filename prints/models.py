from django.db import models
from django.urls import reverse

from print_tracker.settings.common import AUTH_USER_MODEL


class Filament(models.Model):
    material = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.material}'


def get_or_create_a_deleted_filament():
    """
    Gets an existing `Filament` object or creates a new `Filament` object which has `material` attribute of `deleted`. The [0] gets the first element of the QuerySet.
    """
    return Filament.objects.get_or_create(material='deleted')[0]


class ModelPrint(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='prints',
        on_delete=models.CASCADE
    )
    filament = models.ForeignKey(
        Filament,
        related_name='prints',
        on_delete=models.SET(
            get_or_create_a_deleted_filament
        )
    )

    def __str__(self):
        return (
            f'{self.id} : '
            f'{self.name} : '
            f'{self.creator.username} : '
            f'{self.filament.material if self.filament else "No filament provided"}'
        )
    
    def get_absolute_url(self):
        return reverse('prints:model_detail', args=(self.pk,))

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'
