from django.db import models

class CreateAccount(models.Model):

    surname = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    email = models.EmailField(blank = True)
    phone = models.CharField(max_length = 13)
    password = models.CharField(max_length = 100)

    """def __str__(self):
        
        return self.surname, self.name, self.email, self.phone, self.password"""