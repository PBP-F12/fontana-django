from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        AUTHOR = "AUTHOR", 'Author'
        READER = "READER", 'Reader'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    full_name = models.CharField(max_length=255, null=True, blank=True)

    @property
    def is_reader(self):
        return self.role == self.Role.READER

    def save(self, *args, **kwargs):
        if not self.pk:  # if user doesn't have a primary key, or if user hasn't been created then...
            self.role = self.base_role
            return super().save(*args, **kwargs)


class AuthorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.AUTHOR)


class Author(User):
    base_role = User.Role.AUTHOR

    author = AuthorManager()

    class Meta:
        proxy = True  # prevent generate class table in database


class ReaderManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.READER)


class Reader(User):
    base_role = User.Role.READER

    author = ReaderManager()

    class Meta:
        proxy = True  # prevent generate class table in database
