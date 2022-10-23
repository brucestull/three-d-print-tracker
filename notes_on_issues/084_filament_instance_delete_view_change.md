# `FilamentInstanceDeleteView` only when no `ModelPrint`

## Resources:

## Current UX:

1. User enters URL `prints/filament-instances/2/delete/` manually since link doesn't show on web page:

1. User is presented dialog with `Confirm Delete` button:

1. User clicks `Confirm Delete` button:

1. User is presented `Server Error (500)`:

## Proposed resolution:

1. Add check `not hasattr(filament_instance, 'print')` to `test_func()`:
    ```
    def test_func(self):
        filament_instance = self.get_object()
        return (
            # User is `FilamentRoll` `owner`:
            self.request.user == filament_instance.filament_roll.owner
            and
            # `FilamentInstance` has no associated `ModelPrint`s:
            not hasattr(filament_instance, 'print')
        )
    ```