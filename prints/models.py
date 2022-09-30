from django.db import models

from print_tracker.settings.common import AUTH_USER_MODEL


class Filament(models.Model):
    material = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.material}'


class ModelPrint(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(AUTH_USER_MODEL, related_name='prints', on_delete=models.CASCADE)
    filament = models.ForeignKey(Filament, related_name='prints', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id} : {self.name} : {self.creator.username} : {self.filament.material if self.filament else "No filament provided"}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'
