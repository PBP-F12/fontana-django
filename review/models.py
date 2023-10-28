from django.db import models
from auths.models import Reader
from main.models import Book

# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.IntegerField()

    def __str__(self) -> str:
        return self.user_id.name + ' - ' + self.book_id.title

    class Meta:
        db_table = 'review' 
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'