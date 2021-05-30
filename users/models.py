from django.db import models
from django.contrib.auth.models import User

import uuid


def default_account_preferences():
    return {}


def default_account_data():
    return {}


class Account(models.Model):
    
    """
        Account instance extends the capability of the base User model to implement additional features
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    preferences = models.JSONField(default=default_account_preferences)
    data = models.JSONField(default=default_account_data)
    

    def __str__(self):
        return f'Account: {self.uuid}, {self.user.get_full_name()}, {self.user.email}'

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'