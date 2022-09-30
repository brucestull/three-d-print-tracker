# Experiment with Model Method `SET()`

## Process:

### Set up Implementation:

1. Use [`SET()`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.SET) as guide to edit [`prints/models.py`](../prints/models.py):
    * Add `get_deleted_filament` method:
        ```
        #...
        def get_deleted_filament():
            return Filament.objects.get_or_create(material='deleted')[0]
        #...
        ```
    * Modify `on_delete` attribute:
        ```
        on_delete=models.SET(
            get_deleted_filament
        )
        ```
    * **NOTE:** This implementation will either use an already existing `Filament` object which has `deleted` as `material` or creates one.

### Test out the implementation Locally:

1. Code is written so we can test in Django Admin Interface.

1. Ensure development server is running.
    * http://localhost:8000/admin/

1. Create `Filament` with `material` of `Filamant to Delete`:
    * http://localhost:8000/admin/prints/filament/add/
    * `id`: 11
    * `material`: `Filamant to Delete`

1. Create `ModelPrint` which uses the `Filament` created above:
    * http://localhost:8000/admin/prints/modelprint/add/
    * `name`: `Filament should change to 'deleted'.`
    * `creator`: `admin`
    * `filament`: `11 : Filament to Delete`
    * After creation:
        * `id`: 10

1. Verify `ModelPrint` properties:
    * Verified same as above.

1. Open Django Admin Interface for newly created `Filament` (id=11) above:
    * http://localhost:8000/admin/prints/filament/11/change/

1. Click `Delete` button for the newly created `Filament` (id=11) above:
    * http://localhost:8000/admin/prints/filament/11/delete/

1. Observe internet browser text:
    ```
    Are you sure?
    Are you sure you want to delete the filament "11 : Filamant to Delete"? All of the following related items will be deleted:

    Summary
    Filaments: 1
    Objects
    Filament: 11 : Filamant to Delete
    ```

1. Click `Yes, I'm sure` button.

1. Operation suceeded:
    * No new `Filament` object was created.
    * Existing material=10 object was used, I think.

1. Check `ModelPrint` object with id=10:
    * http://localhost:8000/admin/prints/modelprint/10/change/
    * The `ModelPrint` object uses the `Filament` object (material='deleted') with id=10.

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0007_alter_modelprint_filament.py
            - Alter field filament on modelprint
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0007_alter_modelprint_filament... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Push to Heroku:
    ```
    remote:   Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
    remote:   Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    remote: Operations to perform:
    remote:   Apply all migrations: admin, auth, contenttypes, prints, sessions, users
    remote: Running migrations:
    remote:   No migrations to apply.
    remote:   Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
    remote:   Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
    remote: Waiting for release.... done.
    To https://git.heroku.com/flynnt-knapp-print-tracker.git
       0220695..a4bfb89  main -> main
    PS C:\Users\Bruce\Programming\see-3d>
    ```

1. Run `manage.py makemigrations` on Heroku:
    * `heroku run python manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py makemigrations
        Running python manage.py makemigrations on ⬢ flynnt-knapp-print-tracker... up, run.7995 (Hobby)
        Migrations for 'prints':
          prints/migrations/0007_alter_modelprint_filament.py
            - Alter field filament on modelprint
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Run `manage.py migrate` on Heroku:
    * `heroku run python manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate
        Running python manage.py migrate on ⬢ flynnt-knapp-print-tracker... up, run.5758 (Hobby)
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          No migrations to apply.
          Your models in app(s): 'prints' have changes that are not yet reflected in a migration, and so won't be applied.
          Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Forgot to commit the migration:
    ```
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            prints/migrations/0007_alter_modelprint_filament.py
    ```

1. Push to Heroku:
    * Success!

### Test out the implementation on Heroku:

1. Create a new `Filament` object:
    * `material`: `Filament To Delete`
    * `id`: 7
    * URL:
        * https://flynnt-knapp-print-tracker.herokuapp.com/admin/prints/filament/7/change/

1. Create a new `ModelPrint` object which uses above `Filament`:
    * `name`: `Filament should change to 'deleted'.`
    * `creator`: `NotAnAdmin`
    * `Filament`: `7 : Filament To Delete`
    * URL:
        * https://flynnt-knapp-print-tracker.herokuapp.com/admin/prints/modelprint/9/change/

1. Delete the `Filament` with `id` of `7`:
    * Model Change URL:
        * https://flynnt-knapp-print-tracker.herokuapp.com/admin/prints/filament/7/change/
    * Model Delete URL:
        * https://flynnt-knapp-print-tracker.herokuapp.com/admin/prints/filament/7/delete/
            ```
            Are you sure?
            Are you sure you want to delete the filament "7 : Filament To Delete"? All of the following related items will be deleted:

            Summary
            Filaments: 1
            Objects
            Filament: 7 : Filament To Delete
            ```
    * Accept `Yes, I'm sure`.

1. New `Filament`:
    * `material`: `deleted`
    * `id`: 8
    * URL:
        * https://flynnt-knapp-print-tracker.herokuapp.com/admin/prints/filament/8/change/

1. `ModelPrint` now has newly created `Filament` (id=8) above as it's associated `Filament`:
    * https://flynnt-knapp-print-tracker.herokuapp.com/admin/prints/modelprint/9/change/

1. Implementation seems to work for now.

1. Proceed to [Create `ModelPrint` `DetailView`](./06_create_model_print_detail_view.md)


## Repository Links:
* Back to [Add `Filament` `ForeignKey` to `ModelPrint`](./04_add_filament_foreign_key_to_model_print.md)
* [README.md](../README.md)