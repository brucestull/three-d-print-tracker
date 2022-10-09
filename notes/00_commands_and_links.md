# Useful Commands and Links

## Commands:

### `pipenv`:
* `pipenv install`
    * Create a `pipenv` virtual environment for the current directory.
* `pipenv install django==4.0`
* `pipenv install django==4.1`
* `pipenv install docutils==0.19`
* `pipenv shell`
* `exit`
    * Exit the current `pipenv` virtual environment.

### `pip`:
* `pip list`

### Django:
* `django-admin startproject the_project .`
* `python .\manage.py startapp the_app`
* `python .\manage.py runserver`
* `<Ctrl+C>`
* `python .\manage.py makemigrations users`
* `python .\manage.py makemigrations accounts`
* `python .\manage.py makemigrations`
* `python .\manage.py migrate`
* `python .\manage.py createsuperuser`
* `python .\manage.py createsuperuser --email admin@email.app --username admin`
* `python .\manage.py runserver`

### Django Create `SECRET_KEY`:
* `python manage.py shell`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`

### Heroku:
* `git push heroku main`
* Can't have leading `.\` when running command with `heroku run`:
    * `heroku run python manage.py createsuperuser --email admin@email.app --username admin`
* `heroku login`
* `heroku run python manage.py migrate users`
* `heroku run python manage.py migrate`

### PowerShell:
* `Get-Command python | Format-List *`

### Misc:
* `tree /f /a`

### Git:
* `git remote -v`

## Production deployment links:
* Dashboard:
    * https://dashboard.heroku.com/apps
* Server Root:
    * https://flynnt-knapp-print-tracker.herokuapp.com/
* Models Home:
    * http://flynnt-knapp-print-tracker.herokuapp.com/prints/
* Create user:
* Django Admin:
* Django Admin Documentation:

## Development server web links:
* Server Root:
    * http://localhost:8000/
* Accounts:
    * http://localhost:8000/accounts/signup/
    * http://localhost:8000/accounts/login/
    * http://localhost:8000/accounts/logout/
    * http://localhost:8000/accounts/password_reset/
    * http://localhost:8000/accounts/reset/Mg/set-password/
* Filament Rolls:

* Models Home:

* Django Admin:
    * http://localhost:8000/admin/
* Django Admin Documentation:
    * http://localhost:8000/admin/doc/
    * http://localhost:8000/admin/doc/tags/
    * http://localhost:8000/admin/doc/filters/
    * http://localhost:8000/admin/doc/models/
    * http://localhost:8000/admin/doc/models/auth.user/

## Repository Links:
* Repository [`README.md`](../README.md).