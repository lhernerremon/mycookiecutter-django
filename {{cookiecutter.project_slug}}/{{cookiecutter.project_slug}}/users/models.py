# Django
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db import models

# Models Utils
from model_utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    """Default user for Codebase Django."""

    email = models.EmailField("Correo electrónico", unique=True)
    # name = models.CharField("Nombre completo", blank=True, max_length=255)
    # first_name = None  # type: ignore
    # last_name = None  # type: ignore
    raw_password = models.CharField("Unencrypted password", max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.get_full_name() or self.get_username() or self.email

    def set_password(self, raw_password):
        """Overwrite this method because we need to save the raw password to send the welcome mail with the password """
        self.password = make_password(raw_password)
        self._password = raw_password
        self.raw_password = raw_password

    class Meta:
        get_latest_by = "created"
        ordering = ["-created", "-modified"]
