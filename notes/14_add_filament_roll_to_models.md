# Add `FilamentRoll` to `models.py`

## NOTES:
* Current code in [`prints/models.py`](../prints/models.py) is using [`models.SET()`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.SET) for learning purposes. This option will be changed in the future to some more sophisticated solution.

## Process:

1. Change `material` to `filament_roll` in [`prints/models.py`](../prints/models.py) and other project files:
    * [`prints/models.py`](../prints/models.py)
    * [`templates/model_print_detail.html`](../templates/model_print_detail.html)
    * [`templates/model_print_list.html`](../templates/model_print_list.html)

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Was filamentinstance.material renamed to filamentinstance.filament_roll (a CharField)? [y/N] y
        Migrations for 'prints':
          prints\migrations\0011_filamentroll_and_more.py
            - Create model FilamentRoll
            - Rename field material on filamentinstance to filament_roll
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0011_filamentroll_and_more... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Add `FilamentRoll` model to [`prints/admin.py`](../prints/admin.py):
    ```
    #...
    from .models import FilamentRoll
    #...

    #...
    admin.site.register(FilamentRoll)
    #...
    ```

1. Test local server version.

1. Edit `FilamentInstance` in [`prints/models.py`](../prints/models.py):
    ```
    class FilamentInstance(models.Model):
        """
        Model for the `prints.filamentinstance` used in `prints.modelprint`.
        """
        filament_roll = models.ForeignKey(
            FilamentRoll,
            on_delete=models.PROTECT,
        )

        def __str__(self):
            return f'{self.id} : {self.filament_roll}'
    ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0012_alter_filamentinstance_filament_roll.py
            - Alter field filament_roll on filamentinstance
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        django.db.utils.IntegrityError: The row in table 'prints_filamentinstance' with primary key '1' has an invalid foreign key: prints_filamentinstance.filament_roll_id contains a value 'PLA' that does not have a corresponding value in prints_filamentroll.id.
        ```

1. Change `filament_roll`, in database `prints_filamentinstance`, to `1`.

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0012_alter_filamentinstance_filament_roll... OK
          Applying prints.0013_alter_filamentinstance_filament_roll... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Current state of [`prints/models.py`](../prints/models.py):
    * `FilamentRoll`:
        ```
        class FilamentRoll(models.Model):
            """
            Model for the `prints.filamentroll` used in each `prints.filamentinstance` instance.
            Need to figure out a way to make a unique 'id'.
            Might use 'choices', in future, for 'material'.
            """
            material = models.CharField(max_length=255)

            def __str__(self):
                return f'{self.id} : {self.material}'
        ```

    * `get_or_create_a_deleted_filament_roll`:
        ```
        def get_or_create_a_deleted_filament_roll():
            """
            Gets an existing `prints.filamentroll` object or creates a new `prints.filamentroll` object which has `material` attribute of `deleted`. The [0] gets the first element of the QuerySet.
            """
            return FilamentRoll.objects.get_or_create(material='deleted')[0]
        ```

    * `FilamentInstance`:
        ```
        class FilamentInstance(models.Model):
            """
            Model for the `prints.filamentinstance` used in `prints.modelprint`.
            """
            # filament_roll = models.CharField(max_length=255)
            filament_roll = models.ForeignKey(
                FilamentRoll,
                on_delete=models.SET(
                    get_or_create_a_deleted_filament_roll
                ),
            )

            def __str__(self):
                return f'{self.id} : {self.filament_roll}'
        ```

1. Current state of [`prints/models.py`](../prints/models.py):
    * `FilamentInstance`:
        ```
        class FilamentInstance(models.Model):
            """
            Model for the `prints.filamentinstance` used in `prints.modelprint`.
            """
            material = models.CharField(max_length=255)
            filament_roll = models.ForeignKey(
                FilamentRoll,
                on_delete=models.SET(
                    get_or_create_a_deleted_filament_roll
                ),
            )

            def __str__(self):
                return f'{self.id} : {self.filament_roll}'
        ```

    * `get_or_create_a_deleted_filament_instance`:
        ```
        def get_or_create_a_deleted_filament_instance():
            """
            Gets an existing `prints.filamentinstance` object or creates a new `prints.filamentinstance` object which has `filament_roll` attribute of `deleted`. The [0] gets the first element of the QuerySet.
            """
            return FilamentInstance.objects.get_or_create(material='deleted')[0]
        ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        It is impossible to add a non-nullable field 'material' to filamentinstance without specifying a default. This is because the database needs something to populate existing rows.
        Please select a fix:
         1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
         2) Quit and manually define a default value in models.py.
        Select an option: 1
        Please enter the default value as valid Python.
        The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
        Type 'exit' to exit this prompt
        >>> 'Potato Starch'
        Migrations for 'prints':
          prints\migrations\0014_filamentinstance_material.py
            - Add field material to filamentinstance
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0014_filamentinstance_material... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Lots of issues using [`SET()`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.SET), so a good solution might be to preserve dependencies rather than allow deletion of the fields.
    * Change [Field option](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options)s to [`PROTECT`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.PROTECT).
    * [`RESTRICT`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.RESTRICT) might be a better option.
        * This will involve use of [`CASCADE`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.CASCADE).

1. Current state of [`prints/models.py`](../prints/models.py):
    ```
    class Manufacturer(models.Model):
        """
        Model for the `prints.manufacturer` of a `prints.filamentinstance` object.
        """
        name = models.CharField(max_length=255)

        def __str__(self):
            return f'{self.id} : {self.name}'


    class FilamentRoll(models.Model):
        """
        Model for the `prints.filamentroll` used in each `prints.filamentinstance` instance.
        Need to figure out a way to make a unique 'id'.
        Might use 'choices', in future, for 'material'.
        """
        material = models.CharField(max_length=255)

        def __str__(self):
            return f'{self.id} : {self.material}'


    class FilamentInstance(models.Model):
        """
        Model for the `prints.filamentinstance` used in `prints.modelprint`.
        """
        filament_consumed = models.FloatField(default=0)
        filament_roll = models.ForeignKey(
            FilamentRoll,
            on_delete=models.PROTECT,
        )

        def __str__(self):
            return f'{self.id} : {self.filament_roll.material}'


    class ModelPrint(models.Model):
        """
        Model for each instance of a printed 3D object.
        """
        name = models.CharField("Name of 3D Print Model", max_length=255)
        # created = models.DateTimeField(auto_now_add=True)
        creator = models.ForeignKey(
            AUTH_USER_MODEL,
            related_name='prints',
            on_delete=models.CASCADE,
        )
        filament_instance = models.ForeignKey(
            FilamentInstance,
            related_name='prints',
            on_delete=models.PROTECT,
        )

        def __str__(self):
            return (
                f'{self.id} : '
                f'{self.name} : '
                f'{self.creator.username} : '
                f'{self.filament_instance.filament_roll if self.filament_instance else "No filament_instance provided"}'
            )

        def get_absolute_url(self):
            return reverse('prints:model_detail', args=(self.pk,))
    ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        AttributeError: module 'prints.models' has no attribute 'get_or_create_a_deleted_filament_instance'
        ```

1. Maybe edit `migrations` manually?

1. Migrations modified:
    * [`0007_alter_modelprint_filament.py`](../prints/migrations/0007_alter_modelprint_filament.py):
        ```
        - field=models.ForeignKey(on_delete=models.SET(prints.models.get_or_create_a_deleted_filament_instance), related_name='prints', to='prints.filament'),
        + field=models.ForeignKey(on_delete=models.PROTECT, related_name='prints', to='prints.filament'),
        ```
    * [`0013_alter_filamentinstance_filament_roll.py`](../prints/migrations/0013_alter_filamentinstance_filament_roll.py):
        ```
        - field=models.ForeignKey(on_delete=models.SET(prints.models.get_or_create_a_deleted_filament_roll), to='prints.filamentroll'),
        + field=models.ForeignKey(on_delete=models.PROTECT, to='prints.filamentroll'),
        ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0015_remove_filamentinstance_material_and_more.py
            - Remove field material from filamentinstance
            - Add field filament_consumed to filamentinstance
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0015_remove_filamentinstance_material_and_more... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Test local server version.

1. Push to Heroku:
    * `git push heroku main`
        ```
        django.db.utils.DataError: invalid input syntax for type bigint: "PLA"
        ```

1. Reset Heroku database.

1. Push to Heroku:
    * `git push heroku main`
        ```
        PS C:\Users\Bruce\Programming\see-3d> git push heroku main
        Everything up-to-date
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations on `users`:
    * `heroku run python manage.py migrate users`
        ```
        PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate users
        Running python manage.py migrate users on ⬢ flynnt-knapp-print-tracker... up, run.6946 (Hobby)
        Operations to perform:
          Apply all migrations: users
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0001_initial... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying users.0001_initial... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `heroku run python manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> heroku run python manage.py migrate
        Running python manage.py migrate on ⬢ flynnt-knapp-print-tracker... up, run.6948 (Hobby)
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying prints.0001_initial... OK
          Applying prints.0002_filament... OK
          Applying prints.0003_manufacturer... OK
          Applying prints.0004_modelprint_creator... OK
          Applying prints.0005_modelprint_filament... OK
          Applying prints.0006_alter_modelprint_filament... OK
          Applying prints.0007_alter_modelprint_filament... OK
          Applying prints.0008_alter_modelprint_name... OK
          Applying prints.0009_rename_filament_filamentinstance... OK
          Applying prints.0010_rename_filament_modelprint_filament_instance... OK
          Applying sessions.0001_initial... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Need to create new superuser.
    * `heroku run python manage.py createsuperuser --email admin@email.app --username admin`

1. Some models are not showing in production Django Admin Interface:
    * `FilamentRoll`

1. Try removing all migrations and starting anew.

1. Try migrations as two steps:
    1. Make migrations for `users`:
        * `python .\manage.py makemigrations users`
            ```
            PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations users
            Migrations for 'users':
              users\migrations\0001_initial.py
                - Create model CustomUser
            PS C:\Users\Bruce\Programming\see-3d>
            ```

    1. Make migrations for project:
        * `python .\manage.py makemigrations`
            ```
            PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
            Migrations for 'prints':
              prints\migrations\0001_initial.py
                - Create model FilamentInstance
                - Create model FilamentRoll
                - Create model Manufacturer
                - Create model ModelPrint
                - Add field filament_roll to filamentinstance
            PS C:\Users\Bruce\Programming\see-3d>
            ```

1. Try migrations as one step:
    * Creates an additional migration file `0002_initial.py`. Need to explore this more later.
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0001_initial.py
            - Create model FilamentInstance
            - Create model FilamentRoll
            - Create model Manufacturer
            - Create model ModelPrint
          prints\migrations\0002_initial.py
            - Add field creator to modelprint
            - Add field filament_instance to modelprint
            - Add field filament_roll to filamentinstance
        Migrations for 'users':
          users\migrations\0001_initial.py
            - Create model CustomUser
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Will use two separate migrations:
    1. Make migrations for `users`:
        * `python .\manage.py makemigrations users`
            ```
            PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations users
            Migrations for 'users':
              users\migrations\0001_initial.py
                - Create model CustomUser
            PS C:\Users\Bruce\Programming\see-3d>
            ```
    1. Make migrations for project:
        * `python .\manage.py makemigrations`
            ```
            PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
            Migrations for 'prints':
              prints\migrations\0001_initial.py
                - Create model FilamentInstance
                - Create model FilamentRoll
                - Create model Manufacturer
                - Create model ModelPrint
                - Add field filament_roll to filamentinstance
            PS C:\Users\Bruce\Programming\see-3d>
            ```

1. Perform migrations in one step:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0001_initial... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying users.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying prints.0001_initial... OK
          Applying sessions.0001_initial... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations in two steps:
    * Seems everything follows same order.
    1. `python .\manage.py migrate users`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate users
        Operations to perform:
          Apply all migrations: users
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0001_initial... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying users.0001_initial... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```
    1. `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying prints.0001_initial... OK
          Applying sessions.0001_initial... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Create superuser.

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/

1. Test `Profile` change:
    * Remove 'python manage.py migrate users &&' from 'Procfile'.

1. Push to Heroku:
    * `git push heroku main`
        ```
        PS C:\Users\Bruce\Programming\see-3d> git push heroku main
        Enumerating objects: 31, done.
        Counting objects: 100% (31/31), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (20/20), done.
        Writing objects: 100% (21/21), 4.24 KiB | 2.12 MiB/s, done.
        Total 21 (delta 14), reused 0 (delta 0), pack-reused 0
        remote: Compressing source files... done.
        remote: Building source:
        remote:
        remote: -----> Building on the Heroku-22 stack
        remote: -----> Using buildpack: heroku/python
        remote: -----> Python app detected
        remote: -----> Using Python version specified in Pipfile.lock
        remote: -----> Using cached install of python-3.10.7
        remote: -----> Installing pip 22.2.2, setuptools 63.4.3 and wheel 0.37.1
        remote:        Skipping installation, as Pipfile.lock hasn't changed since last deploy.
        remote: -----> Installing SQLite3
        remote: -----> $ python manage.py collectstatic --noinput
        remote:        128 static files copied to '/tmp/build_5e4ddb1d/staticfiles'.
        remote:
        remote: -----> Discovering process types
        remote:        Procfile declares types -> release, web
        remote:
        remote: -----> Compressing...
        remote:        Done: 45.2M
        remote: -----> Launching...
        remote:  !     Release command declared: this new release will not be available until the command succeeds.
        remote:        Released v35
        remote:        https://flynnt-knapp-print-tracker.herokuapp.com/ deployed to Heroku
        remote:
        remote: Verifying deploy... done.
        remote: Running release command...
        remote:
        remote: Operations to perform:
        remote:   Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        remote: Running migrations:
        remote:   Applying contenttypes.0001_initial... OK
        remote:   Applying contenttypes.0002_remove_content_type_name... OK
        remote:   Applying auth.0001_initial... OK
        remote:   Applying auth.0002_alter_permission_name_max_length... OK
        remote:   Applying auth.0003_alter_user_email_max_length... OK
        remote:   Applying auth.0004_alter_user_username_opts... OK
        remote:   Applying auth.0005_alter_user_last_login_null... OK
        remote:   Applying auth.0006_require_contenttypes_0002... OK
        remote:   Applying auth.0007_alter_validators_add_error_messages... OK
        remote:   Applying auth.0008_alter_user_username_max_length... OK
        remote:   Applying auth.0009_alter_user_last_name_max_length... OK
        remote:   Applying auth.0010_alter_group_name_max_length... OK
        remote:   Applying auth.0011_update_proxy_permissions... OK
        remote:   Applying auth.0012_alter_user_first_name_max_length... OK
        remote:   Applying users.0001_initial... OK
        remote:   Applying admin.0001_initial... OK
        remote:   Applying admin.0002_logentry_remove_auto_add... OK
        remote:   Applying admin.0003_logentry_add_action_flag_choices... OK
        remote:   Applying prints.0001_initial... OK
        remote:   Applying sessions.0001_initial... OK
        remote: Waiting for release.... done.
        To https://git.heroku.com/flynnt-knapp-print-tracker.git
           a67e055..65d601d  main -> main
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Create superuser:
    * `heroku run python manage.py createsuperuser --email admin@email.app --username admin`

1. Proceed to [Convert `ModelPrint` `CreateView` to Function-Based View](./15_convert_create_view_to_function_based.md)

## Repository Links:
* Back to [Change `Filament` to `FilamentInstance`](./13_change_filament_to_filament_instance.md)
* [README.md](../README.md)