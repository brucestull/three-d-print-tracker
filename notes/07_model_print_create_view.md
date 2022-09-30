# Create `ModelPrint` `CreateView`

## Process:

1. Add view `ModelPrintCreateView` to [`prints/views.py`](../prints/views.py):
    ```
    class ModelPrintCreateView(CreateView):
        model = ModelPrint
        template_name ='model_print_create.html'
        fields = ['name', 'creator', 'filament']
    ```

1. Add URL route to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/create/', views.ModelPrintCreateView.as_view(), name='model_create'),
        #...
    ]
    ```

1. Add template [`templates/model_print_create.html`](../templates/model_print_create.html):
    ```
    {% extends "base.html" %}

    {% block title %}Print Tracker - New Model Print{% endblock %}


    {% block content %}

    <h2>Create New Model Print</h2>
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Create New Model Print" />
    </form>

    {% endblock %}
    ```






## Repository Links:
* Back to [Experiment with Model Method `SET()`](./05_experiment_with_model_method_set.md)
* [README.md](../README.md)