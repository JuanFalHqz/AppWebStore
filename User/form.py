from pyexpat import model

from django.forms import ModelForm

from User.models import User


class UserChangePasswordForm(ModelForm):
    class Meta:
        model= User
        fields='__all__'

class UserForm(ModelForm):
    class Meta:
        model= User
        fields='__all__'