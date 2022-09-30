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








## Repository Links:
* Back to [Add `AUTH_USER_MODEL` `ForeignKey` to `ModelPrint`](./03_add_user_foreign_key_to_model_print.md)
* [README.md](../README.md)