from django.db import models

class CreateAccount(models.Model):
    surname = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    password = models.CharField(max_length = 100)