# Project Directory Structure

* `tree /f /a`:  
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> tree /f /a
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
    +---images
    |       database_planning_01.png
    |       database_planning_02.png
    |       database_planning_03.png
    |       database_planning_04.png
    |
    +---notes
    |       00_application_planning.md
    |       00_commands_and_links.md
    |       00_directory_structure.md
    |       00_model_planning.md
    |       01_create_initial_model_versions.md
    |       02_model_print_list_view.md
    |       03_add_user_foreign_key_to_model_print.md
    |       04_add_filament_foreign_key_to_model_print.md
    |       05_experiment_with_model_method_set.md
    |       06_model_print_detail_view.md
    |       07_model_print_create_view.md
    |       08_model_update_view.md
    |       09_model_print_delete_view.md
    |       10_require_login_for_create_model_print.md
    |       11_require_ownership_for_model_print_update.md
    |       12_require_ownership_for_model_print_delete.md
    |       13_change_filament_to_filament_instance.md
    |       14_add_filament_roll_to_models.md
    |       15_convert_create_view_to_function_based.md
    |       16_filament_roll_create_view.md
    |       99_fix_manage_py_check_deploy_warnings.md
    |       README.md
    |
    +---notes_setup
    |       01_create_repository_from_template.md
    |       02_run_application_locally.md
    |       03_create_heroku_application_server_instance.md
    |       04_provision_database_server_instance.md
    |       05_add_django_settings_module_to_config_vars.md
    |       06_add_secret_key_to_config_vars.md
    |       07_add_database_settings_to_config_vars.md
    |       08_modify_allowed_hosts.md
    |       09_push_to_heroku_and_createsuperuser.md
    |       README.md
    |
    +---prints
    |   |   admin.py
    |   |   apps.py
    |   |   forms.py
    |   |   models.py
    |   |   tests.py
    |   |   urls.py
    |   |   views.py
    |   |   __init__.py
    |   |
    |   \---migrations
    |           0001_initial.py
    |           0002_alter_filamentinstance_filament_roll.py
    |           0003_alter_filamentroll_manufacturer.py
    |           0004_filamentroll_creator.py
    |           0005_rename_creator_filamentroll_owner.py
    |           __init__.py
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
    |   |   filament_roll_create.html
    |   |   filament_roll_delete.html
    |   |   filament_roll_detail.html
    |   |   filament_roll_edit.html
    |   |   filament_roll_list.html
    |   |   home.html
    |   |   model_print_create.html
    |   |   model_print_delete.html
    |   |   model_print_detail.html
    |   |   model_print_edit.html
    |   |   model_print_list.html
    |   |
    |   \---registration
    |           login.html
    |           signup.html
    |           update.html
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

    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```


## Repository Links:
[README.md](../README.md)
