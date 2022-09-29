from print_tracker.settings.common import *


DEBUG = True


ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Create your own `SECRET_KEY` here for use in Development. Create a specific one for production only and use it in production only.
SECRET_KEY = "3)hq&x!awji5*(iw3ovzji^92as-nw57(m@7h#x^-c2wzu%qam"

# To create a new `SECRET_KEY`:
"""
    python .\manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""