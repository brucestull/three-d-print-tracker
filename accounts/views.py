from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from accounts.forms import CustomUserCreationForm
from accounts.forms import CustomUserChangeForm

from accounts.models import CustomUser

class SignUpView(CreateView):
    """
    View for user to create a new account.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserUpdateView(UpdateView):
    """
    View for user to update an existing account.
    """
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name ='registration/update.html'