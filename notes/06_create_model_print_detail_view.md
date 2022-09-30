# Create `ModelPrint` `DetailView`

## Process:

1. Add `ModelPrintDetailView` view to [`prints/views.py`](../prints/views.py):
    ```
    from django.views.generic import DetailView

    class ModelPrintDetailView(DetailView):
        model = ModelPrint
        template_name ='model_print_detail.html'
    ```

1. Add URL route to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/<int:pk>/', views.ModelPrintDetailView.as_view(), name='model_detail'),
        #...
    ]
    ```

1. Add template [`templates/model_print_detail.html`](../templates/model_print_detail.html):
    * `modelprint` or `object` context variables will both work.
    ```
    {% extends "base.html" %}

    {% block title %}Print Tracker - {{ object.name }}{% endblock %}


    {% block content %}

    <h2>Model Detail</h2>
    {{ object.name }}<br>
    {{ object.filament.material }}<br>
    {{ object.creator.username }}<br>

    {% endblock %}
    ```
    **OR**
    ```
    {% extends "base.html" %}

    {% block title %}Print Tracker - {{ modelprint.name }}{% endblock %}


    {% block content %}

    <h2>Model Detail</h2>
    {{ modelprint.name }}<br>
    {{ modelprint.filament.material }}<br>
    {{ modelprint.creator.username }}<br>

    {% endblock %}
    ```

1. We now have a simple detail view. We can add more functionality later.

1. Proceed to 


## Repository Links:
* Back to [Experiment with Model Method `SET()`](./05_experiment_with_model_method_set.md)
* [README.md](../README.md)