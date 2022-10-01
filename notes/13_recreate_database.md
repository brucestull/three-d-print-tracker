# Recreate Database
* Made some changes to [`prints/models.py`](../prints/models.py) that wrecked database and I don't have the ability to fix it quite yet so resetting the database.
* Will document [`prints/models.py`](../prints/models.py) changes after resetting the database.

## Process:


1. Make migrations:
    * `python .\manage.py makemigrations users`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations users
        Migrations for 'users':
          users\migrations\0001_initial.py
            - Create model CustomUser
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Make migrations:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0001_initial.py
            - Create model FilamentInstance
            - Create model Manufacturer
            - Create model ModelPrint
            - Create model FilamentRoll
            - Add field filament_roll to filamentinstance
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
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

1. Create superuser:
    * `python .\manage.py createsuperuser --email admin@email.app --username admin`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py createsuperuser --email admin@email.app --username admin
        Password:
        Password (again):
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Test development server:
    * `python .\manage.py runserver`
    * http://localhost:8000/




1. Proceed to 

## Repository Links:
* Back to [Require Ownership of `ModelPrint` to Delete the Instance](./12_require_ownership_for_model_print_delete.md)
* [README.md](../README.md)
