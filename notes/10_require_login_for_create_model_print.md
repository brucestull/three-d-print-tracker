# Require Login for `ModelPrint` `CreateView`

## Resources:
* [`django.views.generic.edit.FormView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView)

## Process:

1. Add import of `LoginRequiredMixin` from `django.contrib.auth.mixins` to [`prints/views.py`](../prints/views.py):

1. Modify view `ModelPrintCreateView` in [`prints/views.py`](../prints/views.py):
    1. Implement multiple inherits `LoginRequiredMixin` and `CreateView`:
        ```
        #...
        class ModelPrintCreateView(LoginRequiredMixin, CreateView):
        #...
        ```
    1. Add [`form_valid()`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView) method:
        ```
        def form_valid(self, form):
            """
            Set `form.instance.creator` as `self.request.user` when valid form data is provided.
            """
            form.instance.creator = self.request.user
            return super().form_valid(form)
        ```

1. Edit templates to hide or show links as appropriate.
    * [`templates/base.html`](../templates/base.html)
    * [`templates/home.html`](../templates/home.html)
    * [`templates/model_print_detail.html`](../templates/model_print_detail.html)

1. Proceed to [Require Ownership of `ModelPrint` to Update the Properties](./11_require_ownership_for_model_print_update.md)

## Repository Links:
* Back to [Create `ModelPrint` `DeleteView`](./09_model_print_delete_view.md)
* [README.md](../README.md)
