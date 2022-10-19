# Add Ownership Requirements to `FilamentRoll` Update View

## Links:
* [Add ownership requirements to update and delete views](https://github.com/brucestull/three-d-print-tracker/issues/77)

## `FilamentRoll` Update View:

### Current State:
* Users who are not `FilamentRoll.owner` can edit `FilamentRoll` properties.

### Functional Changes:

1. Add `UserPassesTestMixin` and `test_func()` to class `FilamentRollUpdateView` in [`prints/views.py`](../prints/views.py):
    ```
    class FilamentRollUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = FilamentRoll
        template_name = 'filament_rolls/filament_roll_edit.html'
        fields = [
        'manufacturer',
        'material',
        ]
    
        def test_func(self):
            roll = self.get_object()
            print('roll: ', roll)
            return self.request.user == roll.owner
    ```

1. When user is not `FilamentRoll.owner`, they get `403 Forbidden` when attempting the edit view:
    * http://localhost:8000/prints/rolls/ROLL_ID/edit/

1. Remove edit link from page if user doesnt' own the roll.

1. Modify [`templates/filament_rolls/filament_roll_detail.html`](../templates/filament_rolls/filament_roll_detail.html):
    ```
    {% if user.id == filamentroll.owner.id %}
        <a href={% url 'prints:roll_edit' filamentroll.id %}>Edit Roll: {{ filamentroll }}</a><br>
    {% endif %}
    ```

1. `FilamentRoll` edit link is now not available to `FilamentRoll` non-owners.