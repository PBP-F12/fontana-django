from django.contrib.auth.forms import UserCreationForm
from .models import User, Author, Reader


class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class AuthorRegistrationForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ('username', 'password')


class ReaderRegistrationForm(UserCreationForm):
    class Meta:
        model = Reader
        fields = ('username', 'password')
