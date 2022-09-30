# Create `ModelPrint` `DeleteView`

## Process:

1. Add import for `DeleteView` from `django.views.generic.edit` to [`prints/views.py`](../prints/views.py):
    ```
    #...
    from django.views.generic.edit import DeleteView
    #...
    ```

1. Add import for `reverse_lazy` from `django.urls` to [`prints/views.py`](../prints/views.py):
    ```
    #...
    from django.urls import reverse_lazy
    #...
    ```

1. Add view `ModelPrintDeleteView` to [`prints/views.py`](../prints/views.py):
    ```
    class ModelPrintDeleteView(DeleteView):
        model = ModelPrint
        template_name ='model_print_delete.html'
        success_url = reverse_lazy('prints:home')
    ```

1. Add URL route to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/<int:pk>/delete/', views.ModelPrintDeleteView.as_view(), name='model_delete'),
        #...
    ]
    ```

1. Add template [`templates/model_print_delete.html`](../templates/model_print_delete.html):
    * This page is used for delete confirmation.
    ```
    {% extends "base.html" %}

    {% block title %}Print Tracker - Delete {{ modelprint.name }}{% endblock %}

    {% block content %}

    <h2>Delete Model Print</h2>
    <form action="" method="post">
        {% csrf_token %}
        <p>Do you really want to delete "{{ modelprint.name }}"?</p>
        <input type="submit" value="Confirm Delete" />
    </form>

    {% endblock %}
    ```

1. Add delete link to template [`templates/model_print_detail.html`](../templates/model_print_detail.html):
    ```
    <a href={% url 'prints:model_delete' modelprint.id %}>Delete this Model Print</a><br>
    ```

1. Proceed to 

## Repository Links:
* Back to [Create `ModelPrint` `UpdateView`](./08_model_update_view.md)
* [README.md](../README.md)