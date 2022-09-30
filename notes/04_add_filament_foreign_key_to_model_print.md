# Add `Filament` `ForeignKey` to `ModelPrint`

## Process:

1. Add `Filament` `ForeignKey` to `ModelPrint`:
    ```
    class ModelPrint(models.Model):
        #...
        filament = models.ForeignKey(Filament, related_name='prints', null=True, on_delete=models.SET_NULL)
        #...
    ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0005_modelprint_filament.py
            - Add field filament to modelprint
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0005_modelprint_filament... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. **NOTE:** Probably didn't have to specify any relationships for migration since `null=True` is argument for `filament`.

1. Try:
    * `filament = models.ForeignKey(Filament, related_name='prints', on_delete=models.PROTECT)`

1. This only allows deletion of a `Filament` object if it is not already associated with a `ModelPrint` object.

1. Try again:
    * `filament = models.ForeignKey(Filament, related_name='prints', null=True, on_delete=models.SET_NULL)`

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        No changes detected
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. It seems that migrations are not necessary since the model attribute `null=True` is handled by Django code and not database settings?

1. Perform migrations (probably won't do anything since previous step didn't change migrations):
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          No migrations to apply.
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. As expected, previous step not needed.

1. Attempt to delete a `Filament` which is already associated with a `ModelPrint`:

1. `Filament` deleted.

1. Attempt to see `ModelPrint` view in Django Admin Interface:
    * Internet browser output:
        * `Exception Value:	'NoneType' object has no attribute 'material'`
            * Since `Filament` is deleted, the `Filament` object is now `NoneType` (`NULL` in database).
            * And a `NoneType` does not have a `material` attribute.

1. Error in console:
    ```
      File "C:\Users\Bruce\Programming\see-3d\prints\models.py", line 19, in __str__
        return f'{self.id} : {self.name} : {self.creator.username} : {self.filament.material}'
    AttributeError: 'NoneType' object has no attribute 'material'
    ```
    * Fix dunder string of `ModelPrint`.

1. It was more informative to use console output to troubleshoot than to use browser error output.


1. Current `filament` attribute and new dunder string for `ModelPrint`:
    ```
    class ModelPrint(models.Model):
        #...
        filament = models.ForeignKey(Filament, related_name='prints', null=True, on_delete=models.SET_NULL)
        #...

        #...
        def __str__(self):
            return f'{self.id} : {self.name} : {self.creator.username} : {self.filament.material if self.filament else "No filament provided"}'
        #...
    ```

1. Above code allows deletion of `Filament` objects. But it may be better to preserve database since if a `Filament` is used by a `ModelPrint` object, it makes sense to still require the `Filament`:
    * So, will refactor code to keep `Filament`.
    * Will keep current form of dunder string since it helped me learn.

1. Current `filament` attribute and new dunder string for `ModelPrint`:
    ```
    filament = models.ForeignKey(
        Filament,
        related_name='prints',
        on_delete=models.PROTECT
    )
    ```

1. Had some issues. Learned a bit.

1. Tried some stuff:
<details>
<summary>Sample output:</summary>

    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py makemigrations
    Running python manage.py makemigrations on ⬢ flynnt-knapp-print-tracker... up, run.2647 (Hobby)
    It is impossible to change a nullable field 'filament' on modelprint to non-nullable without providing a default. This is because the database needs something to populate existing rows.
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
     3) Quit and manually define a default value in models.py.
    Select an option: ^[[A^H^H^H^H^H^H^H
    Please select a valid option: 2
    Migrations for 'prints':
      prints/migrations/0006_alter_modelprint_filament.py
        - Alter field filament on modelprint
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate
    Running python manage.py migrate on ⬢ flynnt-knapp-print-tracker... up, run.8383 (Hobby)
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, prints, sessions, users
    Running migrations:
      No migrations to apply.
      Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
      Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py makemigrations
    Running python manage.py makemigrations on ⬢ flynnt-knapp-print-tracker... up, run.5052 (Hobby)
    It is impossible to change a nullable field 'filament' on modelprint to non-nullable without providing a default. This is because the database needs something to populate existing rows.
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
     3) Quit and manually define a default value in models.py.
    Select an option: 2
    Migrations for 'prints':
      prints/migrations/0006_alter_modelprint_filament.py
        - Alter field filament on modelprint
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate
    Running python manage.py migrate on ⬢ flynnt-knapp-print-tracker... up, run.9285 (Hobby)
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, prints, sessions, users
    Running migrations:
      No migrations to apply.
      Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
      Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run manage.py makemigrations prints
    Running manage.py makemigrations prints on ⬢ flynnt-knapp-print-tracker... up, run.3185 (Hobby)
    bash: line 1: manage.py: command not found
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py makemigrations prints
    Running python manage.py makemigrations prints on ⬢ flynnt-knapp-print-tracker... up, run.6716 (Hobby)
    It is impossible to change a nullable field 'filament' on modelprint to non-nullable without providing a default. This is because the database needs something to populate existing rows.
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
     3) Quit and manually define a default value in models.py.
    Select an option: 2
    Migrations for 'prints':
      prints/migrations/0006_alter_modelprint_filament.py
        - Alter field filament on modelprint
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py makemigrations
    Running python manage.py makemigrations on ⬢ flynnt-knapp-print-tracker... up, run.5514 (Hobby)
    It is impossible to change a nullable field 'filament' on modelprint to non-nullable without providing a default. This is because the database needs something to populate existing rows.
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
     3) Quit and manually define a default value in models.py.
    Select an option: 2
    Migrations for 'prints':
      prints/migrations/0006_alter_modelprint_filament.py
        - Alter field filament on modelprint
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate prints
    Running python manage.py migrate prints on ⬢ flynnt-knapp-print-tracker... up, run.9828 (Hobby)
    Operations to perform:
      Apply all migrations: prints
    Running migrations:
      No migrations to apply.
      Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
      Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate
    Running python manage.py migrate on ⬢ flynnt-knapp-print-tracker... up, run.4505 (Hobby)
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, prints, sessions, users
    Running migrations:
      No migrations to apply.
      Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
      Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py makemigrations prints
    Running python manage.py makemigrations prints on ⬢ flynnt-knapp-print-tracker... up, run.9242 (Hobby)
    It is impossible to change a nullable field 'filament' on modelprint to non-nullable without providing a default. This is because the database needs something to populate existing rows.
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
     3) Quit and manually define a default value in models.py.
    Select an option: 2
    Migrations for 'prints':
      prints/migrations/0006_alter_modelprint_filament.py
        - Alter field filament on modelprint
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate
    Running python manage.py migrate on ⬢ flynnt-knapp-print-tracker... up, run.6515 (Hobby)
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, prints, sessions, users
    Running migrations:
      No migrations to apply.
      Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
      Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d>
    PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate prints
    Running python manage.py migrate prints on ⬢ flynnt-knapp-print-tracker... up, run.5678 (Hobby)
    Operations to perform:
      Apply all migrations: prints
    Running migrations:
      No migrations to apply.
      Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
      Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    PS C:\Users\Bruce\Programming\see-3d>
</details>

1. Try migrations locally again.

1. Make migrations:
    * `python .\manage.py makemigrations prints`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations prints
        It is impossible to change a nullable field 'filament' on modelprint to non-nullable without providing a default. This is because the database needs something to populate existing rows.
        Please select a fix:
         1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
         2) Ignore for now. Existing rows that contain NULL values will have to be handled manually, for example with a RunPython or RunSQL operation.
         3) Quit and manually define a default value in models.py.
        Select an option: 1
        Please enter the default value as valid Python.
        The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
        Type 'exit' to exit this prompt
        >>> 2
        Migrations for 'prints':
          prints\migrations\0006_alter_modelprint_filament.py
            - Alter field filament on modelprint
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        No changes detected
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0006_alter_modelprint_filament... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. `Filament`s are currently set up so they can't be deleted if they are associated with a `ModelPrint`. This may change in the future.
    * Possible changes:
        * Use [`SET_DEFAULT`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.SET_DEFAULT) and set a default.
            * What to use for default:
                * Create a `Filament` object in database and use it?
        * Use [`SET_NULL`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.SET_NULL) but this will allow a `NULL` value, which is weird for me right now since I don't know how to handle those cases yet.
        * Use [`SET()`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.SET):
            * This seems like a great solution.
                ```
                Set the ForeignKey to the value passed to SET(), or if a callable is passed in, the result of calling it. In most cases, passing a callable will be necessary to avoid executing queries at the time your models.py is imported:

                from django.conf import settings
                from django.contrib.auth import get_user_model
                from django.db import models

                def get_sentinel_user():
                    return get_user_model().objects.get_or_create(username='deleted')[0]

                class MyModel(models.Model):
                    user = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.SET(get_sentinel_user),
                    )
                ```

1. Proceed to [Experiment with Model Method `SET()`](./05_experiment_with_model_method_set.md)

## Repository Links:
* Back to [Add `AUTH_USER_MODEL` `ForeignKey` to `ModelPrint`](./03_add_user_foreign_key_to_model_print.md)
* [README.md](../README.md)