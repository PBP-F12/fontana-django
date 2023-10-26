from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['author_id', 'avg_rating', 'num_ratings']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['book_cover_file'].required = False  # Specify that the field is not required
