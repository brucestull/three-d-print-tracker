from django.urls import path

from . import views

app_name = 'prints'
urlpatterns = [
    path('', views.ModelPrintListView.as_view(), name='model_prints'),
    path('print/<int:pk>/', views.ModelPrintDetailView.as_view(), name='model_detail'),
]
