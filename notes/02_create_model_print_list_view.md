# Create `ModelPrint` List View

## Process:

1. Add `ModelPrintListView` view to [](../prints/views.py):
    ```
    from django.views.generic import ListView

    from .models import ModelPrint


    class ModlePrintListView(ListView):
        """
        Class-based view, which inherits from `django.views.generic.ListView`, to provide list view of model `ModelPrint`.
        """
        model = ModelPrint
        template_name = 'model_print_list.html'
    ```

1. Add route for `prints` app to project root URL file [`print_tracker/urls.py`](../print_tracker/urls.py):
    ```
    urlpatterns = [
        #...
        path('prints/', include('prints.urls'), name='prints'),
        #...
    ]
    ```

1. Create [`prints/urls.py`](../prints/urls.py) and add `app_name` and route for list view:
    ```
    from django.urls import path

    from . import views

    app_name = 'prints'
    urlpatterns = [
        path('', views.ModelPrintListView.as_view(), name='model_prints'),
    ]
    ```

1. Create list view `ModelPrintListView` for `ModelPrint` to [`prints/views.py`](../prints/views.py):
    ```
    from django.views.generic import ListView

    from .models import ModelPrint

    class ModelPrintListView(ListView):
        """
        Class-based view, which inherits from `django.views.generic.ListView`, to provide list view of model `ModelPrint`.
        """
        model = ModelPrint
        template_name = 'model_print_list.html'
    ```

1. Create template [`templates/model_print_list.html`](../templates/model_print_list.html) and add context object variables to access `object_list`:
    ```
    {% extends "base.html" %}
    
    {% block title %}Print Tracker - Models Home{% endblock %}
    
    
    {% block content %}
    
    {{ object_list }}
    
    {% for model in object_list %}
    <p>{{ model }}</p>
    {% endfor %}
    
    {% endblock %}
    ```




## Repository Links:
* Back to [Create Initial Model Versions](./01_create_initial_model_versions.md)
* [README.md](../README.md)