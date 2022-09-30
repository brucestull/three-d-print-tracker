# Create `ModelPrint` `UpdateView`

## Process:

1. Add view `ModelPrintUpdateView` to [`prints/views.py`](../prints/views.py):
    ```
    from django.views.generic.edit import UpdateView

    class ModelPrintUpdateView(UpdateView):
        model = ModelPrint
        template_name ='model_print_update.html'
        fields = ['name', 'creator', 'filament']
    ```

1. Add URL route to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/<int:pk>/edit/', views.ModelPrintUpdateView.as_view(), name='model_update'),
        #...
    ]
    ```

1. Add template [`templates/model_print_update.html`](../templates/model_print_update.html):
    ```
    {% extends "base.html" %}

    {% block title %}Print Tracker - New Model Print{% endblock %}
    
    {% block content %}

    <h2>Update Model Print</h2>
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Update Model Print" />
    </form>

    {% endblock %}
    ```

1. Simple `ModelPrint` `UpdateView` completed.

1. Proceed to [Create `ModelPrint` `DeleteView`](./09_model_print_delete_view.md)

## Repository Links:
* Back to [Create `ModelPrint` `CreateView`](./07_model_print_create_view.md)
* [README.md](../README.md)
