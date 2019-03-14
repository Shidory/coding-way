from django.db import models
from django.contrib.auth.password_validation import password_changed
from django.db.models.fields import CharField
from unittest.util import _MAX_LENGTH

class CreateAccount(models.Model):
    surname = models.CharField(_MAX_LENGTH = 100)
    name = models.CharField(_MAX_LENGTH = 100)
