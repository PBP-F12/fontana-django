from django.contrib.auth.forms import UserCreationForm
from .models import User, Author, Reader


class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'full_name')


class AuthorRegistrationForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ('username', 'full_name')


class ReaderRegistrationForm(UserCreationForm):
    class Meta:
        model = Reader
        fields = ('username', 'full_name')
