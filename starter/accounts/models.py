from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    last_activity = models.DateTimeField(_("last activity"), null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-last_login"]

    def __str__(self):
        return self.get_full_name() or self.username
