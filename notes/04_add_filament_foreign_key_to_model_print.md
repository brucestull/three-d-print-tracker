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





## Repository Links:
* Back to [Add `AUTH_USER_MODEL` `ForeignKey` to `ModelPrint`](./03_add_user_foreign_key_to_model_print.md)
* [README.md](../README.md)