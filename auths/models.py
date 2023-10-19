from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        AUTHOR = "AUTHOR", 'Author'
        READER = "READER", 'Reader'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:  # if user doesn't have a primary key, or if user hasn't been created then...
            self.role = self.base_role
            return super().save(*args, **kwargs)
