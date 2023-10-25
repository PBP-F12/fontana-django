from django import forms
from main.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # add all model fields to form

        # exclude these fields from form
        exclude = ['author_id', 'avg_rating', 'num_rating']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['book_cover_file'].required = False
