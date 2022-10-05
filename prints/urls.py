from django.urls import path

from . import views

app_name = 'prints'
urlpatterns = [
    path('', views.ModelPrintListView.as_view(), name='home'),

    path(
        'print/model-print-form-view/',
        views.ModelPrintFormView.as_view(),
        name='model_print_form_view',
    ),

    path(
        'print/model-print-create-view/',
        views.ModelPrintCreateView.as_view(),
        name='model_print_create_view'
    ),

    path(
        'print/create-model-print/',
        views.model_print_create_function,
        name='create_model_print'
    ),
    path(
        'print/create-filament-roll/',
        views.create_filament_roll,
        name='create_filament_roll'
    ),

    path(
        'print/<int:pk>/',
        views.ModelPrintDetailView.as_view(),
        name='model_detail'
    ),
    path(
        'print/<int:pk>/edit/',
        views.ModelPrintUpdateView.as_view(),
        name='model_update'
    ),
    path(
        'print/<int:pk>/delete/',
        views.ModelPrintDeleteView.as_view(),
        name='model_delete'
    ),
]
