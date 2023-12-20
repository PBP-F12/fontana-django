from django.db import models
from auths.models import Reader
from main.models import Book
import uuid


class Bookmark(models.Model):
    bookmark_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True)
    user_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
