from django.db import models

#model for user details
class NewUser(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.firstname