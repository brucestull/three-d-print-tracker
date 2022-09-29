# 09 - Push to Heroku and Create Superuser

## Resources:

## Process:

1. Git `push` to `heroku`:  
    `git push heroku main`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> git push heroku main
        Enumerating objects: 412, done.
        Counting objects: 100% (412/412), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (175/175), done.
        Writing objects: 100% (412/412), 138.32 KiB | 138.32 MiB/s, done.
        Total 412 (delta 241), reused 399 (delta 232), pack-reused 0
        remote: Compressing source files... done.
        remote: Building source:
        remote:
        remote: -----> Building on the Heroku-20 stack
        remote: -----> Determining which buildpack to use for this app
        remote: -----> Python app detected
        remote: -----> Using Python version specified in Pipfile.lock
        remote: cp: cannot stat '/tmp/build_02de82b2/requirements.txt': No such file or directory
        remote: -----> Installing python-3.10.5
        remote: -----> Installing pip 22.1.2, setuptools 60.10.0 and wheel 0.37.1
        remote: -----> Installing dependencies with Pipenv 2020.11.15
        remote:        Installing dependencies from Pipfile.lock (16fbc4)...
        remote:        Ignoring tzdata: markers 'sys_platform == "win32"' don't match your environment
        remote: -----> Installing SQLite3
        remote: -----> $ python manage.py collectstatic --noinput
        remote:        128 static files copied to '/tmp/build_02de82b2/staticfiles'.
        remote:
        remote: -----> Discovering process types
        remote:        Procfile declares types -> release, web
        remote:
        remote: -----> Compressing...
        remote:        Done: 45.1M
        remote: -----> Launching...
        remote:  !     Release command declared: this new release will not be available until the command succeeds.
        remote:        Released v14
        remote:        https://totally-new-heroku-app-name.herokuapp.com/ deployed to Heroku
        remote:
        remote: Verifying deploy... done.
        remote: Running release command...
        remote:
        remote: Operations to perform:
        remote:   Apply all migrations: users
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
        remote: Operations to perform:
        remote:   Apply all migrations: admin, auth, contenttypes, sessions, users
        remote: Running migrations:
        remote:   Applying admin.0001_initial... OK
        remote:   Applying admin.0002_logentry_remove_auto_add... OK
        remote:   Applying admin.0003_logentry_add_action_flag_choices... OK
        remote:   Applying sessions.0001_initial... OK
        remote: Waiting for release.... done.
        To https://git.heroku.com/totally-new-heroku-app-name.git
        * [new branch]      main -> main
        ```

1. Log in to Heroku CLI if not already logged in:  
    `heroku login`

1. Create superuser:  
    `heroku run python manage.py createsuperuser`

1. Follow `createsuperuser` dialog.

1. Log in to deployed application:
    * Sample application address:  
        * https://totally-new-heroku-app-name.herokuapp.com/

1. Add your own functionality to the application.

## Repository Links:
[README.md](../README.md)