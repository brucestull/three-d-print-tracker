# `FilamentInstance` Update and Deletion Views and Templates Require Something

## Links:
* [`FilamentInstance` update and deletion views and templates require something](https://github.com/brucestull/three-d-print-tracker/issues/79)

## Functional Changes:

1. Add `UserPassesTestMixin` and `test_func()` to class `FilamentInstanceUpdateView` in [`prints/views.py`](../prints/views.py):
    ```
    def test_func(self):
        filament_instance = self.get_object()
        print('filament_instance: ', filament_instance)
        print('Can we update filament_instance?: ', self.request.user == filament_instance.filament_roll.owner)
        return self.request.user == filament_instance.filament_roll.owner
    ```

1. The application now restricts the view `FilamentInstanceUpdateView` to only the associated `FilamentRoll` `owner`. But there is still a link presented to all users for the view. Non-owner of `FilamentRoll` gets `403 Forbidden` when clicking 'edit' button.

1. Need to show `FilamentInstance` 'edit' button only for `FilamentRoll` owner.

1. Edit [`templates/filament_instances/filament_instance_detail.html`](../templates/filament_instances/filament_instance_detail.html):
    ```
    {% if filamentinstance.filament_roll.owner == user %}
    <a href={% url 'prints:filament_instance_edit' filamentinstance.id %}>
        Edit Filament Instance
    </a>
    {% endif %}
    ```

1. Edit `FilamentInstance` link now shows only for `owner` of associated `FilamentRoll`.
