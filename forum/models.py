from django.db import models
import uuid
from main.models import Book
from django.utils import timezone
from auths.models import Reader

# Create your models here.


class Forum(models.Model):
    forum_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    forum_creator_id = models.ForeignKey(Reader, on_delete=models.CASCADE)

    forum_title = models.CharField(max_length=256)
    forum_discussion = models.TextField(null=True)
    book_topic = models.ForeignKey(Book, on_delete=models.CASCADE)

    num_comments = models.IntegerField(default=0, editable=False)


class ForumReply(models.Model):
    reply_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    commentor_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    forum_id = models.ForeignKey(Forum, on_delete=models.CASCADE)

    text = models.TextField()
    date_uploaded = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.date_uploaded = timezone.now()

        return super(ForumReply, self).save(*args, **kwargs)
