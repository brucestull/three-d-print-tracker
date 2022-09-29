# 02 - Run Application Locally

## Resources:

## Process:

1. Project root directory:
    * `C:\Users\Bruce\Programming\see-3d\`

1. `pipenv install`
    * Console output:
        ```
        PS C:\Users\Bruce\Programming\see-3d> pipenv install
        Creating a virtualenv for this project...
        Pipfile: C:\Users\Bruce\Programming\see-3d\Pipfile
        Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.7) to create virtualenv...
        [ ===] Creating virtual environment...created virtual environment CPython3.10.7.final.0-64 in 2930ms
          creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\see-3d-8mKp-VtJ, clear=False, no_vcs_ignore=False, global=False)
          seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
            added seed packages: pip==22.2.2, setuptools==65.3.0, wheel==0.37.1
          activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

        Successfully created virtual environment!
        Virtualenv location: C:\Users\Bruce\.virtualenvs\see-3d-8mKp-VtJ
        Installing dependencies from Pipfile.lock (69aa94)...
          ================================ 9/9 - 00:00:10
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. `pipenv shell`
    * Console output:
        ```
        PS C:\Users\Bruce\Programming\see-3d> pipenv shell
        Launching subshell in virtual environment...
        PowerShell 7.2.6
        Copyright (c) Microsoft Corporation.

        https://aka.ms/powershell
        Type 'help' to get help.

        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. `python manage.py migrate`
    * Console output:
        ```
        PS C:\Users\Bruce\Programming\see-3d> python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions, users
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
          Applying sessions.0001_initial... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. `python .\manage.py createsuperuser --email admin@email.app --username admin`
    * Console output:
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py createsuperuser --email admin@email.app --username admin
        Password:
        Password (again):
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. `python .\manage.py runserver`
    * Sample terminal output on server start:
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        September 29, 2022 - 08:31:31
        Django version 4.0, using settings 'print_tracker.settings.development'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
        ```

1. http://localhost:8000/

1. http://localhost:8000/admin/

1. Investigate the Django Admin Documentation features:
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/models/users.customuser/

1. Proceed to [Create Heroku Application Server Instance](03_create_heroku_application_server_instance.md).


## Repository Links:
[README.md](../README.md)