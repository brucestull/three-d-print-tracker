from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A CustomUser class is added so we can add functionality later. It's more convenient then not to add CustomUser at beginning of project before database migrations are started.
    """
    is_supermaker = models.BooleanField(
        default=False,
        help_text=(
            'Designates whether the user is a Supermaker. '
            'Supermakers may gain special privileges in the future.'
        )
    )

    def __str__(self):
        """
        String representation of CustomUser.
        """
        return self.username

