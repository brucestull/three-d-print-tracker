from django.urls import path

from users.views import SignUpView
from users.views import UserUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/edit/", UserUpdateView.as_view(), name="edit_profile"),
]