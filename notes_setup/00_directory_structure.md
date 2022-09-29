# Project Directory Structure

* `tree /f /a`:  
    ```
    PS C:\Users\Bruce\Programming\see-3d> tree /f /a
    Folder PATH listing for volume OS
    Volume serial number is CC00-DD12
    C:.
    |   .gitignore
    |   db.sqlite3
    |   LICENSE
    |   manage.py
    |   Pipfile
    |   Pipfile.lock
    |   Procfile
    |   README.md
    |
    +---local_things
    |       notes.md
    |
    +---notes_setup
    |       00_commands_and_links.md
    |       00_directory_structure.md
    |       01_create_repository_from_template.md
    |       02_run_application_locally.md
    |       03_create_heroku_application_server_instance.md
    |       04_provision_database_server_instance.md
    |       05_add_django_settings_module_to_config_vars.md
    |       06_add_secret_key_to_config_vars.md
    |       07_add_database_settings_to_config_vars.md
    |       08_modify_allowed_hosts.md
    |       09_push_to_heroku_and_createsuperuser.md
    |
    +---print_tracker
    |   |   asgi.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |   |
    |   \---settings
    |           common.py
    |           development.py
    |           production.py
    |
    +---templates
    |   |   base.html
    |   |   home.html
    |   |
    |   \---registration
    |           login.html
    |           signup.html
    |
    \---users
        |   admin.py
        |   apps.py
        |   forms.py
        |   models.py
        |   tests.py
        |   urls.py
        |   views.py
        |   __init__.py
        |
        \---migrations
                0001_initial.py
                __init__.py
    
    PS C:\Users\Bruce\Programming\see-3d>
    ```


## Repository Links:
[README.md](../README.md)
