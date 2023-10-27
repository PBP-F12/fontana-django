import uuid
from django.db import models

from auths.models import Author

# Create your models here.


class Book(models.Model):
    book_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    author_id = models.ForeignKey(
        Author, on_delete=models.CASCADE, blank=True, null=True)

    book_title = models.CharField(max_length=256)
    description = models.TextField()

    avg_rating = models.FloatField(default=0)
    num_rating = models.IntegerField(default=0, editable=False)

    book_cover_link = models.CharField(max_length=1024, blank=True, null=True)
    book_cover_file = models.ImageField(
        upload_to='upload/book/', blank=True, null=True)

    def __str__(self) -> str:
        return self.book_title
