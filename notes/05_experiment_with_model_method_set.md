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

### Test out the implementation:

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









## Repository Links:
* Back to [Add `Filament` `ForeignKey` to `ModelPrint`](./04_add_filament_foreign_key_to_model_print.md)
* [README.md](../README.md)