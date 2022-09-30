from django.urls import path

from . import views

app_name = 'prints'
urlpatterns = [
    path('', views.ModelPrintListView.as_view(), name='model_prints'),
]
