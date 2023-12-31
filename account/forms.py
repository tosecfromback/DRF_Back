from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SigninForm(UserCreationForm):

    class Meta:
        model = User
        fields = [ '', '' ]


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = [ 'password' ]