from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30)

  
    def name(self):
        return self.first_name + " " + self.last_name