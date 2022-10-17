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

    def get_absolute_url(self):
        return reverse('prints:manufacturer_detail', args=(self.pk,))


class FilamentMaterial(models.Model):
    """
    Model for the `prints.filamentmaterial` of a `prints.filamentinstance`
    object. This model will be used to populate the `FilamentRoll`'s
    'material' and 'meters_per_gram' fields.
    """
    # How many meters of the filament in one gram filament.
    # PLA:.336
    METERS_PER_GRAM = models.DecimalField('Number of meters of Filament in one gram of Filament', max_digits=5, decimal_places=3)
    polymer_type = models.CharField('Polymer type of the Filament (PLA, PLA+, PET, PETG, etc.)', max_length=255)

    def __str__(self):
        return self.polymer_type


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
        # `PROTECT` prevents deletion of `Manufacturer` instance if it
        # is associated with a `FilamentRoll` instance.
        on_delete=models.PROTECT,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='rolls',
        # `CASCADE` allows deletion of `AUTH_USER_MODEL` instance and
        #     also does a cascading deletion of `FilamentRoll` instance.
        # `PROTECT` prevents deletion of `AUTH_USER_MODEL` instance if
        #     it is associated with a `FilamentRoll` instance.
        # `SET_NULL` Set the ForeignKey null; this is only possible if
        #     null is True. We do this here so a user can be deleted
        #     but their `FilamentRoll` instances stay. This may change
        #     in future.
        on_delete=models.SET_NULL,
        null=True,
    )
    material = models.ForeignKey(
        FilamentMaterial,
        related_name='rolls',
        # `PROTECT` prevents deletion of `FilamentMaterial` instance if
        #     it is associated with a `FilamentRoll` instance.
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'[ {self.material} ] {self.manufacturer.name} #{self.id}'

    def get_absolute_url(self):
        return reverse('prints:roll_detail', args=(self.pk,))


class FilamentInstance(models.Model):
    """
    Model for the `prints.filamentinstance` used in `prints.modelprint`.
    """
    # 0.337
    # 0.336
    # 0.334
    # 0.333
    # 0.338
    # -----
    # 0.336
    METERS_PER_GRAM = .336
    FILAMENT_CONSUMED_PRECISION = 2
    grams_filament_consumed = models.IntegerField(default=0)
    filament_roll = models.ForeignKey(
        FilamentRoll,
        related_name='instances',
        # `PROTECT` prevents deletion of `FilamentRoll` instance if it
        #     is associated with a `FilamentInstance` instance.
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{self.grams_filament_consumed} grams of {self.filament_roll}'

    def get_absolute_url(self):
        return reverse('prints:filament_instance_detail', args=(self.pk,))

    def meters_filament_consumed(self):
        """
        Meters used for `FilamentInstance`.

        This uses the calculated value for PLA (`METERS_PER_GRAM`). Need to allow for different polymer types.
        """
        return round(self.grams_filament_consumed * self.METERS_PER_GRAM, self.FILAMENT_CONSUMED_PRECISION)


class ModelPrint(models.Model):
    """
    Model for each instance of a printed 3D object.
    """
    name = models.CharField("Name of 3D Print Model", max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='prints',
        # `CASCADE` allows deletion of `AUTH_USER_MODEL` instance and
        #     also does a cascading deletion of `ModelPrint`.
        on_delete=models.CASCADE,
    )
    filament_instance = models.OneToOneField(
        FilamentInstance,
        related_name='print',
        # `PROTECT` prevents deletion of `FilamentInstance` instance
        #     if it is associated with a `ModelPrint` instance.
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return (
            self.name
        )
    
    def get_absolute_url(self):
        return reverse('prints:model_detail', args=(self.pk,))
