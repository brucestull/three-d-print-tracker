# Require Ownership of `ModelPrint` to Delete the Instance

## Resources:
* [`test_func()`](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin.test_func)

## Process:

1. Ensure import of `UserPassesTestMixin` from `django.contrib.auth.mixins` exists:
    ```
    from django.contrib.auth.mixins import UserPassesTestMixin
    ```

1. Implement multiple inheritances for `ModelPrintDeleteView` in [`prints/views.py`](../prints/views.py):
    * `LoginRequiredMixin`
    * `UserPassesTestMixin`
    * `UpdateView`
        ```
        #...
        class ModelPrintDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        #...
        ```

1. Add `test_func()` to `ModelPrintDeleteView`:
    ```
    def test_func(self):
        """
        Returns `True` if `self.request.user` is `model_print.creator`. In other words, returns `True` if the user requesting to delete the `ModelPrint` is the user who is associated with the `ModelPrint`.
        """
        model_print = self.get_object()
        return self.request.user == model_print.creator
    ```

1. Proceed to 

## Repository Links:
* Back to [Require Ownership of `ModelPrint` to Update the Properties](./11_require_ownership_for_model_print_update.md)
* [README.md](../README.md)
