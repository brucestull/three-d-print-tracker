# Create Initial Model Versions

## Process:

1. Create `print_tracker` application:
    * `python .\manage.py startapp prints`

1. Directory structure:
    * `tree /f /a prints`
        ```
        PS C:\Users\Bruce\Programming\see-3d> tree /f /a prints
        Folder PATH listing for volume OS
        Volume serial number is CC00-DD12
        C:\USERS\BRUCE\PROGRAMMING\SEE-3D\PRINTS
        |   admin.py
        |   apps.py
        |   models.py
        |   tests.py
        |   views.py
        |   __init__.py
        |
        \---migrations
                __init__.py

        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Add `prints.apps.PrintsConfig` application to `INSTALLED_APPS` attribute in [`print_tracker/settings/common.py`](../print_tracker/settings/common.py):
    ```
    INSTALLED_APPS = [
        #...
        'prints.apps.PrintsConfig',
        #...
    ]
    ```

1. Add `ModelPrint` model to [`prints/models.py`](../prints/models.py):
    ```
    from django.db import models
    
    class ModelPrint(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
            return f"{self.id} : {self.name}"
    ```

1. Register `ModelPrint` in [`prints/admin.py`](../prints/admin.py):
    ```
    from django.contrib import admin
    from .models import ModelPrint
    
    admin.site.register(ModelPrint)
    ```

1. Make migrations for the project:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0001_initial.py
            - Create model ModelPrint
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`

1. Start development server:
    * `python .\manage.py runserver`

1. Test Django Admin Interface:
    * Django Admin:
        * http://localhost:8000/admin/

1. Add a few `ModelPrint`s:
    * http://localhost:8000/admin/prints/
    * http://localhost:8000/admin/prints/modelprint/
    * http://localhost:8000/admin/prints/modelprint/add/

1. Add `Filament` model to [`prints/models.py`](../prints/models.py):
    ```
    #...
    class Filament(models.Model):
        material = models.CharField(max_length=255)
    
        def __str__(self):
            return f"{self.id} : {self.material}"
    #...
    ```

1. Register `Filament` in [`prints/admin.py`](../prints/admin.py):
    ```
    #...
    from .models import Filament
    #...

    #...
    admin.site.register(Filament)
    #...
    ```

1. Make migrations for the project:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0002_filament.py
            - Create model Filament
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0002_filament... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Start development server:
    * `python .\manage.py runserver`

1. Test Django Admin Interface:
    * Django Admin:
        * http://localhost:8000/admin/


1. Add a few `Filament`s:
    * http://localhost:8000/admin/prints/
    * http://localhost:8000/admin/prints/filament/
    * http://localhost:8000/admin/prints/filament/add/

1. Add `Manufacturer` model to [`prints/models.py`](../prints/models.py):
    ```
    class Manufacturer(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
            return f'{self.id} : {self.name}'
    ```

1. Register `Manufacturer` in [`prints/admin.py`](../prints/admin.py):
    ```
    #...
    from .models import Manufacturer
    #...

    #...
    admin.site.register(Manufacturer)
    #...
    ```

1. Make migrations for the project:
    * `python .\manage.py makemigrations`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py makemigrations
        Migrations for 'prints':
          prints\migrations\0003_manufacturer.py
            - Create model Manufacturer
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Perform migrations:
    * `python .\manage.py migrate`
        ```
        PS C:\Users\Bruce\Programming\see-3d> python .\manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, prints, sessions, users
        Running migrations:
          Applying prints.0003_manufacturer... OK
        PS C:\Users\Bruce\Programming\see-3d>
        ```

1. Start development server:
    * `python .\manage.py runserver`

1. Test Django Admin Interface:
    * Django Admin:
        * http://localhost:8000/admin/

1. Add a few `Manufacturer`s:
    * http://localhost:8000/admin/prints/
    * http://localhost:8000/admin/prints/manufacturer/
    * http://localhost:8000/admin/prints/manufacturer/add/

1. Proceed to [Create `ModelPrint` List View](./02_create_model_print_list_view.md)

## Repository Links:
* [README.md](../README.md)