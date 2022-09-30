# Add `AUTH_USER_MODEL` `ForeignKey` to `ModelPrint`

## Process:

1. Add import to [](../prints/models.py):
    ```
    from print_tracker.settings.common import AUTH_USER_MODEL}
    ```

1. Add `ForeignKey` to `ModelPrint`:
    ```
    class ModelPrint(models.Model):
        #...
        creator = models.ForeignKey(AUTH_USER_MODEL, related_name='prints', on_delete=models.CASCADE)
        #...

    ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        It is impossible to add a non-nullable field 'creator' to modelprint without specifying a default. This is because the database needs something to populate existing rows.
        Please select a fix:
         1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
         2) Quit and manually define a default value in models.py.
        Select an option: 1
        Please enter the default value as valid Python.
        The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
        Type 'exit' to exit this prompt
        >>> from users.models import CustomUser
        Invalid input: invalid syntax (<string>, line 1)
        >>> 1
        Migrations for 'prints':
          prints\migrations\0004_modelprint_creator.py
            - Add field creator to modelprint
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0004_modelprint_creator... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Proceed to [Add `Filament` `ForeignKey` to `ModelPrint`](./04_add_filament_foreign_key_to_model_print.md)


## Repository Links:
* Back to [Create `ModelPrint` List View](./02_create_model_print_list_view.md)
* [README.md](../README.md)