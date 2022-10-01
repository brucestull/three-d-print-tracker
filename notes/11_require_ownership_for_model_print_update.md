# Require Ownership of `ModelPrint` to Update the Properties

## Resources:

## Process:

1. Add import of `UserPassesTestMixin` from `django.contrib.auth.mixins`:
    ```
    from django.contrib.auth.mixins import UserPassesTestMixin
    ```

1. Implement multiple inheritances for `ModelPrintUpdateView` in [`prints/views.py`](../prints/views.py):
    * `LoginRequiredMixin`
    * `UserPassesTestMixin`
    * `UpdateView`
        ```
        #...
        class ModelPrintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        #...
        ```

1. Remove `creator` from `fields` attribute of `ModelPrintUpdateView`:
    ```
    #...
    fields = ['name', 'filament']
    #...
    ```

1. Add `test_func()` to `ModelPrintUpdateView`:
    ```
    def test_func(self):
        """
        Returns `True` if `self.request.user` is `model_print.creator`. In other words, returns `True` if the user requesting to update the `ModelPrint` is the user who is associated with the `ModelPrint`.
        """
        model_print = self.get_object()
        return self.request.user == model_print.creator
    ```

1. Proceed to 

## Repository Links:
* Back to [Require Login for `ModelPrint` `CreateView`](./10_require_login_for_create_model_print.md)
* [README.md](../README.md)
