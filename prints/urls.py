from django.urls import path

from . import views

app_name = 'prints'
urlpatterns = [
    path('', views.ModelPrintListView.as_view(), name='home'),
    path('print/create/', views.ModelPrintCreateView.as_view(), name='model_create'),
    path('print/<int:pk>/', views.ModelPrintDetailView.as_view(), name='model_detail'),
    path('print/<int:pk>/edit/', views.ModelPrintUpdateView.as_view(), name='model_update'),
    path('print/<int:pk>/delete/', views.ModelPrintDeleteView.as_view(), name='model_delete'),
]
