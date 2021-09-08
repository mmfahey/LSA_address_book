from django.db import models
from django.db.models.fields import CharField
from django.conf import settings

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)


