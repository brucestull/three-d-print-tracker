from django.db import models


class ModelPrint(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'


class Filament(models.Model):
    material = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.material}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'
