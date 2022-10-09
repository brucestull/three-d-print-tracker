from django.urls import path

from . import views

app_name = 'prints'
urlpatterns = [
    #================================================================
    ## `Manufacturer` Routes:
    path(
        'manufacturers/',
        views.ManufacturerListView.as_view(),
        name='manufacturers',
    ),
    path(
        'manufacturers/<int:pk>/',
        views.ManufacturerDetailView.as_view(),
        name='manufacturer_detail'
    ),
    path(
        'manufacturers/new/',
        views.ManufacturerCreateView.as_view(),
        name='manufacturer_new'
    ),
    path(
        'manufacturers/<int:pk>/edit/',
        views.ManufacturerUpdateView.as_view(),
        name='manufacturer_edit'
    ),
    #================================================================


    #================================================================
    ## `FilamentRoll` Routes:
    path(
        'rolls/',
        views.FilamentRollListView.as_view(),
        name='rolls',
    ),
    path(
        'rolls/<int:pk>/',
        views.FilamentRollDetailView.as_view(),
        name='roll_detail'
    ),
    path(
        'rolls/new/',
        views.FilamentRollCreateView.as_view(),
        name='roll_new'
    ),
    path(
        'rolls/<int:pk>/edit/',
        views.FilamentRollUpdateView.as_view(),
        name='roll_edit'
    ),
    path(
        'rolls/<int:pk>/delete/',
        views.FilamentRollDeleteView.as_view(),
        name='roll_delete'
    ),
    #================================================================


    #================================================================
    ## `FilamentInstance` Routes:
    #================================================================


    #================================================================
    ## `ModelPrint` Routes:
    path(
        'models/',
        views.ModelPrintListView.as_view(),
        name='models'
    ),
    path(
        'models/<int:pk>/',
        views.ModelPrintDetailView.as_view(),
        name='model_detail'
    ),
    path(
        'models/new/',
        views.new_model_print,
        name='model_new'
    ),
    path(
        'models/<int:pk>/edit/',
        views.ModelPrintUpdateView.as_view(),
        name='model_update'
    ),
    path(
        'models/<int:pk>/delete/',
        views.ModelPrintDeleteView.as_view(),
        name='model_delete'
    ),
    #================================================================
]
