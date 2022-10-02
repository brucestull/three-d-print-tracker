# Change `Filament` to `FilamentInstance`

## Process:

### Side Process:

1. Reset database on Heroku.

1. `git push heroku main`

1. `heroku run python manage.py createsuperuser --email admin@email.app --username admin`

1. Test production deployment.

### Actual Appication Development Process:

1. Change `Filament` to `FilamentInstance` in [`prints/models.py`](../prints/models.py):
    ```
    #...
    class FilamentInstance(models.Model):
        #...
    #...


    #...
    def get_or_create_a_deleted_filament():
        #...
        return FilamentInstance.objects.get_or_create(material='deleted')[0]
    #...


    #...
    class ModelPrint(models.Model):
        #...
        filament = models.ForeignKey(
            FilamentInstance,
        #...
        )
    #...
    ```


1. Change `Filament` to `FilamentInstance` in other project files:
    * [`prints/admin.py`](../prints/admin.py)

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Was the model prints.Filament renamed to FilamentInstance? [y/N] y
        Migrations for 'prints':
          prints\migrations\0009_rename_filament_filamentinstance.py
            - Rename model Filament to FilamentInstance
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0009_rename_filament_filamentinstance... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Rename method `models.get_or_create_a_deleted_filament()` to `models.get_or_create_a_deleted_filament_instance()`:
    * [`prints/migrations/0007_alter_modelprint_filament.py`](../prints/migrations/0007_alter_modelprint_filament.py)
    * [`prints/models.py`](../prints/models.py)

1. Push to Heroku:
    * `git push heroku main`

1. Test production deployment.

1. Change `filament` to `filament_instance` in [`prints/models.py`](../prints/models.py) and other project files:
    * [`prints/models.py`](../prints/models.py)
    * [`prints/models.py`](../prints/views.py)
    * [`templates/model_print_detail.html`](../templates/model_print_detail.html)
    * [`templates/model_print_list.html`](../templates/model_print_list.html)




1. Proceed to 

## Repository Links:
* Back to [Require Ownership of `ModelPrint` to Delete the Instance](./12_require_ownership_for_model_print_delete.md)
* [README.md](../README.md)