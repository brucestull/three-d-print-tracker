# Convert `ModelPrint` `CreateView` to Function-Based View

## Resources:
* [`django.views.generic.edit.CreateView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)
* [`django.shortcuts.render()`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#django.shortcuts.render)
* [`django.shortcuts.get_object_or_404()`](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#django.shortcuts.get_object_or_404)
* [`django.http.HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse)
* [`django.http.HttpResponseRedirect`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponseRedirect)
* [`django.urls.reverse()`](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#django.urls.reverse)
* [Working with forms](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-forms)
* [`django.forms.Field`](https://docs.djangoproject.com/en/4.0/ref/forms/fields/#django.forms.Field)
* [`{{ filament_rolls_in_template|length }}`](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#length)
* [`<input>` - www.w3schools.com](https://www.w3schools.com/tags/tag_input.asp)
* [`<input type="number">` - www.w3schools.com](https://www.w3schools.com/tags/att_input_type_number.asp)
* [`<select>` - www.w3schools.com](https://www.w3schools.com/tags/tag_select.asp)

## Process:

1. Add `create_model_print()` to [`prints/views.py`](../prints/views.py):
    ```
    def create_model_print(request):
        return HttpResponse("We're hoping to make a new ModelPrint instance! ...someday...")
    ```

1. Add route `print/create-model-print/` to [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [

        #...
        path('print/create-model-print/', views.create_model_print, name='create_model_print'),
        #...
    ]
    ```

1. Add temporary link to [`templates/base.html`](../templates/base.html):
    ```
    <a
        href={% url 'prints:create_model_print' %}
        >
        Add New 3D Model Print - Function-Based-View
    </a><br>
    ```

1. Start development server:
    * `python .\manage.py runserver`

1. Test `create_model_print`:
    * http://localhost:8000/prints/print/create-model-print/

1. Route and View are connected and functioning.

1. Create `POST` and `GET` logic to handle the request:
    * `POST` should create a new instance of `ModelPrint`.
    * `GET` should render the template.

1. Create template [`templates/model_print_create_function_based.html`](../templates/model_print_create_function_based.html):

1. Modify `create_model_print()` to [`prints/views.py`](../prints/views.py), with comments:
    ```
    def create_model_print(request):
        if request.method == 'POST':

            # # print('POST - request: ', request)
            # print('POST - request.method: ', request.method)
            # # POST - request.method:  POST
            # print('request.POST.keys(): ', request.POST.keys())

            # print("reverse('prints:create_model_print'): ", reverse('prints:create_model_print'))
            # # reverse('prints:create_model_print'):  /prints/print/create-model-print/

            # ##### Do `POST` logic here.

            # #### 1. Maybe have drop-down for `FilamentRoll`. Temporarily use dummy roll:
                # #### Check request.POST.keys():
            # print('request.POST.keys(): ', request.POST.keys())
            # # request.POST.keys():  dict_keys(['csrfmiddlewaretoken', 'model-print-name', 'filament-roll-chosen', 'amount-of-filament-consumed'])

            # Where is this documented?
            # filament_roll_id = request.POST.get('filament-roll-chosen', None)

            filament_roll_id = request.POST.get('filament-roll-chosen')
            print(filament_roll_id)
            # current_filament_roll = FilamentRoll.objects.all()[0]
            current_filament_roll = get_object_or_404(FilamentRoll, pk=filament_roll_id)
            print("current_filament_roll: ", current_filament_roll)
            # # current_filament_roll:  6 : PLA+ : Very First Absolute Roll

            # #### 1. Input for `current_filament_consumed`:
            current_filament_consumed = request.POST.get('amount-of-filament-consumed')
            print("current_filament_consumed: ", current_filament_consumed)

            # #### 1. Get the `model-print-name` value:
            current_model_print_name = request.POST.get('model-print-name')
            print("current_model_print_name: ", current_model_print_name)
            # print('type(current_model_print_name): ', type(current_model_print_name))
            # # type(current_model_print_name):  <class 'str'>

            # #### 1. Create a `FilamentInstance` instance from `amount-of-filament-consumed` and `current_filament_roll`:
            current_filament_instance = FilamentInstance.objects.create(
                filament_consumed=current_filament_consumed,
                filament_roll=current_filament_roll
            )

            # #### 1. Get `current_user`:

            # print("type(current_user): ", type(current_user))
            # # type(current_user):  <class 'users.models.CustomUser'>
            # print("current_user: ", current_user)

            current_user = auth.get_user(request)


            # #### 1. Create a `ModelPrint` instance from `current_model_print_name`, `current_user`, and `current_filament_instance`:
            new_model_print = ModelPrint.objects.create(
                name=current_model_print_name,
                creator=current_user,
                filament_instance=current_filament_instance
            )
            print('new_model_print: ', new_model_print)

            """
            Production Test:
            2022-10-03T14:31:23.037359+00:00 app[web.1]: current_filament_roll:  Hatchbox - PLA+
            2022-10-03T14:31:23.037421+00:00 app[web.1]: current_filament_consumed:  91
            2022-10-03T14:31:23.037472+00:00 app[web.1]: current_model_print_name:  ShayShay
            2022-10-03T14:31:23.052928+00:00 app[web.1]: new_model_print:  5 : ShayShay : FlynntKnapp : Hatchbox - PLA+
            """

            return HttpResponseRedirect(reverse('prints:create_model_print'))


        elif request.method == 'GET':

            # print('GET - request: ', request)
            # # GET - request:  <WSGIRequest: GET '/prints/print/create-model-print/'>
            # print('GET - request.method: ', request.method)
            # # GET - request.method:  GET

            # ##### Do `GET` logic here.
            # #### 1. Get `FilamentRoll` instance(S) information so we can display in a drop-down:
            filament_rolls = FilamentRoll.objects.all()

            # #### 1. Add `filament_rolls` to `context`:
            context = {
                'filament_rolls_in_template': filament_rolls
            }
            # #### 1. Display `FilamenRoll` instance information in a drop-down on template.

            return render(request, 'model_print_create_function_based.html', context)
    ```

1. Current route `print/create-model-print/` in [`prints/urls.py`](../prints/urls.py):
    ```
    urlpatterns = [
        #...
        path('print/create-model-print/', views.create_model_print, name='create_model_print'),
        #...
    ]
    ```

1. Modify links in [`templates/base.html`](../templates/base.html):
    ```
    <a
        href={% url 'prints:create_model_print' %}
        >
        Add New 3D Model Print - Function-Based-View
    </a><br>
    ```

1. Current state of [`templates/model_print_create_function_based.html`](../templates/model_print_create_function_based.html):
    ```
    {% extends "base.html" %}
    
    {% block title %}Print Tracker - New 3D Model Print{% endblock %}
    
    {% block content %}
    
    <h2>Create New 3D Model Print</h2>
    <form action="{% url 'prints:create_model_print' %}" method="post">
        {% csrf_token %}
    
        <label for="model-print-input">Model Print Name</label>
        <input type="text" name="model-print-name" id="model-print-input" placeholder="Model Print Name">
        <br>
    
        {% comment %} Filament Roll Available Attributes: {% endcomment %}
            {% comment %} id {% endcomment %}
            {% comment %} manufacturer {% endcomment %}
            {% comment %} material {% endcomment %}
            {% comment %} filamentinstance_set.all {% endcomment %}
            {% comment %} filamentinstance_set.count {% endcomment %}
        {{ filament_rolls_in_template }}
        <br>
        <label for="filament-rolls-input">Available Filament Rolls: {{ filament_rolls_in_template|length }}</label>
        <select name="filament-roll-chosen" id="filament-rolls-input">
            {% for filament_roll in filament_rolls_in_template %}
            <option value={{ filament_roll.id }}>{{ filament_roll }} : Roll-{{ filament_roll.id }}</option>
            {% endfor %}
        </select>
        <br>
    
        <label for="filament-consumed-input">Amount of Filament Consumed</label>
        <input type="number" name="amount-of-filament-consumed" id="filament-consumed-input" placeholder="Filament Consumed"><br>
    
        <input type="submit" value="Create New 3D Model Print" />
    </form>
    
    {% endblock %}
    ```

1. Convert 'function-based' 'create' view parts in [`prints/views.py`](../prints/views.py) and [`templates/model_print_create_function_based.html`](../templates/model_print_create_function_based.html) to use Django forms.

1. Proceed to []()

## Repository Links:
* Back to [Add `FilamentRoll` to `models.py`](./14_add_filament_roll_to_models.md)
* [README.md](../README.md)