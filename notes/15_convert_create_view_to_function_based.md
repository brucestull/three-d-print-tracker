# Convert `ModelPrint` `CreateView` to Function-Based View

## Resources:
* [`django.views.generic.edit.CreateView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)
* [`django.shortcuts.render()`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#django.shortcuts.render)
* [`django.http.HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse)
* [`django.http.HttpResponseRedirect`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponseRedirect)
* [`django.urls.reverse()`](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#django.urls.reverse)
* [`<input>` - www.w3schools.com](https://www.w3schools.com/tags/tag_input.asp)
* [`<input type="number">` - www.w3schools.com](https://www.w3schools.com/tags/att_input_type_number.asp)

## Process:

1. Add `create_model_print()` to [`prints/views.py`](../prints/views.py):
    ```
    def create_model_print(request):
        return HttpResponse("We're hoping to make a new ModelPrint instance! ...someday...")
    ```

1. Add route `print/create-function-based/` to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [

        #...
        path('print/create-function-based/', views.create_model_print, name='model_create_function_based'),
        #...
    ]
    ```

1. Add temporary link to [`templates/base.html`](../templates/base.html):
    ```
    <a
        href={% url 'prints:model_create_function_based' %}
        >
        Add New 3D Model Print - Function-Based-View
    </a><br>
    ```

1. Start development server:
    * `python .\manage.py runserver`

1. Test `model_create_function_based`:
    * http://localhost:8000/prints/print/create-function-based/

1. Route and View are connected and functioning.

1. Create `POST` and `GET` logic to handle the request:
    * `POST` should create a new instance of `ModelPrint`.
    * `GET` should render the template.

1. Create template []()



1. Proceed to []()

## Repository Links:
* Back to [Add `FilamentRoll` to `models.py`](./14_add_filament_roll_to_models.md)
* [README.md](../README.md)