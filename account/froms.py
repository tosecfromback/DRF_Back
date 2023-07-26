from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterAccount(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'username', 'nickname', 'password', 'password2']

class Login(AuthenticationForm):
    
    class Meta:
        model = User
        fields = [ 'username', 'password']

class UserChange(UserChangeForm):
    
    class Meta:
        model = User
        fields = ['nickname']


class PasswordChange(PasswordChangeForm):
    
    class Meta:
        model = User
        fields = [ 'old_password', 'new_password', 'new_password2']