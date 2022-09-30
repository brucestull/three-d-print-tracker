# Add Django SECRET_KEY to Config Vars

## Resources:

## Process:

1. Next config var is `SECRET_KEY`. We will generate this using Django shell.
    * In terminal session in root of repository, create a key and be prepared to copy it to Heroku application settings "Config Vars":
    
    1. Start Django shell:  
    `python manage.py shell`
    
    1. Import `get_random_secret_key`:  
    `from django.core.management.utils import get_random_secret_key`
    
    1. Use `get_random_secret_key` to get a new key:  
    `print(get_random_secret_key())`
    * Sample output:
        ```
        PS C:\Users\Bruce\Programming\my-local-repository> python .\manage.py shell
        Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>> from django.core.management.utils import get_random_secret_key
        >>> print(get_random_secret_key())
        sm)_qnnxl1*a4r$vtwe%cc%+=t4uyxlqh9d%3_u$=e@oc-)61(
        >>> quit()
        ```

1. Add `SECRET_KEY` as the `KEY` and the output string in previous step as the `VALUE`:
![06_secret_key_entered](https://user-images.githubusercontent.com/47562501/174795061-4b17b4a7-b783-4172-9fed-d8d2db22ad31.png)

1. Click the "Add" button.
![07_click_add_button](https://user-images.githubusercontent.com/47562501/174795089-40708467-30fe-4d36-bf96-f09e5dcb3713.png)

1. Proceed to [Add Database Settings to Config Vars](07_add_database_settings_to_config_vars.md)

## Repository Links:
[README.md](../README.md)