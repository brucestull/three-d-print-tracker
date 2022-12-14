# Rename and Move Templates

## Resources:

## Info:
* Possible default template filepath:
    * `prints/modelprint_list.html`

## Current Directory Structure:
```
\---templates
    |   base.html
    |
    +---filament_instances
    |       filament_instance_create.html
    |       filament_instance_delete.html
    |       filament_instance_detail.html
    |       filament_instance_edit.html
    |       filament_instance_list.html
    |
    +---filament_rolls
    |       filament_roll_create.html
    |       filament_roll_delete.html
    |       filament_roll_detail.html
    |       filament_roll_edit.html
    |       filament_roll_list.html
    |
    +---manufacturers
    |       manufacturer_create.html
    |       manufacturer_delete.html
    |       manufacturer_detail.html
    |       manufacturer_edit.html
    |       manufacturer_list.html
    |
    +---model_prints
    |       model_print_create.html
    |       model_print_delete.html
    |       model_print_detail.html
    |       model_print_edit.html
    |       model_print_list.html
    |
    +---registration
    |       login.html
    |       password_reset_complete.html
    |       password_reset_confirm.html
    |       password_reset_done.html
    |       password_reset_form.html
    |       signup.html
    |       update.html
    |
    \---users_prints
            user_print_profile.html
```

## Process:

1. Move `model_print_*.html` files to [`prints/templates/prints/`](../prints/templates/prints/):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> tree /f /a prints/templates
    Folder PATH listing for volume OS
    Volume serial number is CC00-DD12
    C:\USERS\BRUCE\PROGRAMMING\THREE-D-PRINT-TRACKER\PRINTS\TEMPLATES
    \---prints
            model_print_create.html
            model_print_delete.html
            model_print_detail.html
            model_print_edit.html
            model_print_list.html
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Check `template_name` variables have been changed to reflect new template location in [`prints/views.py`](../prints/views.py):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> Get-ChildItem .\prints\views.py | Select-String template_name | Select-String model_print_
    
    prints\views.py:191:    template_name = 'prints/model_print_list.html'
    prints\views.py:199:    template_name = 'prints/model_print_detail.html'
    prints\views.py:255:    template_name = 'prints/model_print_edit.html'
    prints\views.py:271:    template_name = 'prints/model_print_delete.html'
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Move `filament_instance_*.html` files to [`prints/templates/prints/`](../prints/templates/prints/):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> tree /f /a prints/templates
    Folder PATH listing for volume OS
    Volume serial number is CC00-DD12
    C:\USERS\BRUCE\PROGRAMMING\THREE-D-PRINT-TRACKER\PRINTS\TEMPLATES
    \---prints
            ...
            filament_instance_create.html
            filament_instance_delete.html
            filament_instance_detail.html
            filament_instance_edit.html
            filament_instance_list.html
            ...
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Check `template_name` variables have been changed to reflect new template location in [`prints/views.py`](../prints/views.py):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> Get-ChildItem .\prints\views.py | Select-String template_name | Select-String filament_instance_
    
    prints\views.py:133:    template_name = 'prints/filament_instance_list.html'
    prints\views.py:138:    template_name = 'prints/filament_instance_detail.html'
    prints\views.py:143:    template_name = 'prints/filament_instance_create.html'
    prints\views.py:152:    template_name = 'prints/filament_instance_edit.html'
    prints\views.py:166:    template_name = 'prints/filament_instance_delete.html'
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Move `filament_roll_*.html` files to [`prints/templates/prints/`](../prints/templates/prints/):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> tree /f /a prints/templates
    Folder PATH listing for volume OS
    Volume serial number is CC00-DD12
    C:\USERS\BRUCE\PROGRAMMING\THREE-D-PRINT-TRACKER\PRINTS\TEMPLATES
    \---prints
            ...
            filament_roll_create.html
            filament_roll_delete.html
            filament_roll_detail.html
            filament_roll_edit.html
            filament_roll_list.html
            ...
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Check `template_name` variables have been changed to reflect new template location in [`prints/views.py`](../prints/views.py):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> Get-ChildItem .\prints\views.py | Select-String template_name | Select-String filament_roll_
    
    prints\views.py:76:    template_name = 'prints/filament_roll_list.html'
    prints\views.py:81:    template_name = 'prints/filament_roll_detail.html'
    prints\views.py:86:    template_name = 'prints/filament_roll_create.html'
    prints\views.py:105:    template_name = 'prints/filament_roll_edit.html'
    prints\views.py:119:    template_name = 'prints/filament_roll_delete.html'
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Move `manufacturer_*.html` files to [`prints/templates/prints/`](../prints/templates/prints/):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> tree /f /a prints/templates
    Folder PATH listing for volume OS
    Volume serial number is CC00-DD12
    C:\USERS\BRUCE\PROGRAMMING\THREE-D-PRINT-TRACKER\PRINTS\TEMPLATES
    \---prints
            ...
            manufacturer_create.html
            manufacturer_delete.html
            manufacturer_detail.html
            manufacturer_edit.html
            manufacturer_list.html
            ...
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Check `template_name` variables have been changed to reflect new template location in [`prints/views.py`](../prints/views.py):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> Get-ChildItem .\prints\views.py | Select-String template_name | Select-String manufacturer_
    
    prints\views.py:41:    template_name = 'prints/manufacturer_list.html'
    prints\views.py:46:    template_name = 'prints/manufacturer_detail.html'
    prints\views.py:51:    template_name = 'prints/manufacturer_create.html'
    prints\views.py:59:    template_name = 'prints/manufacturer_edit.html'
    prints\views.py:67:    template_name = 'prints/manufacturer_delete.html'
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Move `user_print_profile.html` file to [`prints/templates/prints/`](../prints/templates/prints/):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> tree /f /a prints/templates
    Folder PATH listing for volume OS
    Volume serial number is CC00-DD12
    C:\USERS\BRUCE\PROGRAMMING\THREE-D-PRINT-TRACKER\PRINTS\TEMPLATES
    \---prints
            ...
            user_print_profile.html
            ...
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```

1. Check `template_name` variables have been changed to reflect new template location in [`prints/views.py`](../prints/views.py):
    ```
    PS C:\Users\Bruce\Programming\three-d-print-tracker> Get-ChildItem .\prints\views.py | Select-String template_name | Select-String user_print_
    
    prints\views.py:286:    template_name = 'prints/user_print_profile.html'
    
    PS C:\Users\Bruce\Programming\three-d-print-tracker>
    ```


