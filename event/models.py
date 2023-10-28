import uuid
from django.db import models
from auths.models import Reader
from main.models import Book

# Create your models here.

class Event(models.Model):
    event_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    event_name = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=1024, blank=True, null=True)
    poster_link = models.CharField(max_length=1024, blank=True, null=True)
    event_date = models.DateField(null=True)
    date = models.DateField(auto_now_add=True)