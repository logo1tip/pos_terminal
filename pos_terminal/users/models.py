from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse


class User(models.Model):

    class UserRole(models.TextChoices):
        ADMINISTRATOR = "AD", _('Administartor')
        COOK = 'CK', _('Cook')
        WAITER = 'WT', _('Waiter')

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    role = models.CharField(
        max_length=2,
        choices=UserRole.choices,
        default=UserRole.ADMINISTRATOR
        )


    def get_absolute_url(self):
        return reverse("user", kwargs={"id": self.id, 'username': self.username})
    