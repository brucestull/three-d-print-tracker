# Push to Heroku and Create Superuser

## Resources:

## Process:

1. Git `push` to `heroku`:  
    `git push heroku main`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\see-3d> git push heroku main
        Enumerating objects: 73, done.
        Counting objects: 100% (73/73), done.
        Delta compression using up to 8 threads
        Compressing objects: 100% (70/70), done.
        Writing objects: 100% (73/73), 38.82 KiB | 19.41 MiB/s, done.
        Total 73 (delta 25), reused 42 (delta 2), pack-reused 0
        remote: Compressing source files... done.
        remote: Building source:
        remote:
        remote: -----> Building on the Heroku-22 stack
        remote: -----> Determining which buildpack to use for this app
        remote: -----> Python app detected
        remote: -----> Using Python version specified in Pipfile.lock
        remote: -----> Installing python-3.10.7
        remote: -----> Installing pip 22.2.2, setuptools 63.4.3 and wheel 0.37.1
        remote: -----> Installing dependencies with Pipenv 2020.11.15
        remote:        Installing dependencies from Pipfile.lock (69aa94)...
        remote: -----> Installing SQLite3
        remote: -----> $ python manage.py collectstatic --noinput
        remote:        128 static files copied to '/tmp/build_097ad8f2/staticfiles'.
        remote:
        remote: -----> Discovering process types
        remote:        Procfile declares types -> release, web
        remote:
        remote: -----> Compressing...
        remote:        Done: 44.8M
        remote: -----> Launching...
        remote:  !     Release command declared: this new release will not be available until the command succeeds.
        remote:        Released v12
        remote:        https://flynnt-knapp-print-tracker.herokuapp.com/ deployed to Heroku
        remote:
        remote: Starting November 28th, 2022, free Heroku Dynos, free Heroku Postgres, and free Heroku Data for Redis® will no longer be available.
        remote:
        remote: If you have apps using any of these resources, you must upgrade to paid plans by this date to ensure your apps continue to run and to retain your data. For students, we will announce a new program by the end of September. Learn more at https://blog.heroku.com/next-chapter
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
        To https://git.heroku.com/flynnt-knapp-print-tracker.git
         * [new branch]      main -> main
        PS C:\Users\Bruce\Programming\see-3d>
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