# 02 - Run Application Locally

## Resources:

## Process:

1. Open terminal in project root:
    * Sample location:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> Get-Location

        Path
        ----
        C:\Users\Bruce\Programming\totally-new-heroku-app-name

        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name>
        ```

1. Create `pipenv` virtual environment using provided `Pipfile` configuration:  
    `pipenv install`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> pipenv install
        Creating a virtualenv for this project...
        Pipfile: C:\Users\Bruce\Programming\totally-new-heroku-app-name\Pipfile
        Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
        [ ===] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 3523ms
        creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM, clear=False, no_vcs_ignore=False, global=False)
        seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
            added seed packages: pip==22.2.2, setuptools==63.2.0, wheel==0.37.1
        activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

        Successfully created virtual environment!
        Virtualenv location: C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM
        Installing dependencies from Pipfile.lock (16fbc4)...
        ================================ 9/9 - 00:00:11
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name>
        ```

1. Note line with `Virtualenv location:`. This line will have the virtual environment location. This information may be useful later.
    * Sample location:
        ```
        C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM
        ```

1. Activate virtual environment:  
    `pipenv shell`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> pipenv shell
        Launching subshell in virtual environment...
        PowerShell 7.2.4
        Copyright (c) Microsoft Corporation.

        https://aka.ms/powershell
        Type 'help' to get help.
        ```

1. Verify current Python interpreter is the one in the virtual environment:  
    `Get-Command python | fl *`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> Get-Command python | fl *

        HelpUri            :
        FileVersionInfo    : File:
                            C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM\Scripts\python.exe
                            InternalName:     Python Launcher
                            OriginalFilename: py.exe
                            FileVersion:      3.10.6
                            FileDescription:  Python
                            Product:          Python
                            ProductVersion:   3.10.6
                            Debug:            False
                            Patched:          False
                            PreRelease:       False
                            PrivateBuild:     False
                            SpecialBuild:     False
                            Language:         Language Neutral

        Path               : C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM\Scripts\python.exe
        Extension          : .exe
        Definition         : C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM\Scripts\python.exe
        Source             : C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM\Scripts\python.exe
        Version            : 3.10.6150.1013
        Visibility         : Public
        OutputType         : {System.String}
        Name               : python.exe
        CommandType        : Application
        ModuleName         :
        Module             :
        RemotingCapability : PowerShell
        Parameters         :
        ParameterSets      :


        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name>
        ```

1. Note that `Path` is (should be) for the Python interpreter which is in the above virtual environment. The Python interpreter is in the `Scripts` directory of the virtual environment we created above.
    * Sample line from above output:
        ```
        Path               : C:\Users\Bruce\.virtualenvs\totally-new-heroku-app-name-D8cdteJM\Scripts\python.exe
        ```

1. Perform `users` application migration. It is important to do the `users` app migration before the rest of the app migrations since we are using a `CustomUser` model which [inherits](https://www.w3schools.com/python/python_inheritance.asp) from `AbstractUser`:  
    `python manage.py migrate users`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> python manage.py migrate users
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
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name>
        ```

1. Perform project migration:  
    `python manage.py migrate`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> python manage.py migrate
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions, users
        Running migrations:
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying sessions.0001_initial... OK
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name>
        ```

1. Create superuser:  
    `python manage.py createsuperuser`
    * Follow `createsuperuser` dialog.
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> python manage.py createsuperuser
            Username: admin
            Email address: admin@email.app
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            PS C:\Users\Bruce\Programming\totally-new-heroku-app-name>
            ```

1. Test application on local server:  
    `python manage.py runserver`
    * Sample terminal output on server start:
        ```
        PS C:\Users\Bruce\Programming\totally-new-heroku-app-name> python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        August 19, 2022 - 10:03:05
        Django version 4.0, using settings 'my_current_project.settings.development'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
        ```

1. Open browser to server address:
    * http://localhost:8000/

1. Login using superuser credentials created above.

1. Investigate Django Admin interface:
    * http://localhost:8000/admin/

1. Investigate the Django Admin Documentation features:
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/models/users.customuser/

1. Proceed to [Create Heroku Application Server Instance](03_create_heroku_application_server_instance.md).


## Repository Links:
[README.md](../README.md)