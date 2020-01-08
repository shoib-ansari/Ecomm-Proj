from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # userref = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.BigIntegerField(null=True)
    alt_contact = models.BigIntegerField(null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=500,null=True)
    postal_add = models.BigIntegerField(null=True)

    def __srt__(self):
        return self.username


