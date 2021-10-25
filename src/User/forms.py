from django import forms
from django.contrib.auth.forms import UserCreationForm
from User.models import CustomUser
from django.contrib.auth import get_user_model


class SigninForm(forms.Form):
    email = forms.EmailField(max_length=45, required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)


#class SignupForm(forms.Form):
#    username = forms.CharField(max_length=200, required=True)
#    email = forms.EmailField(max_length=45, required=True)
#    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
#    cgu_accept = forms.BooleanField(initial=True)

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #model = get_user_model()
        model = CustomUser
        #fields = ('username', 'email')
        fields = ("email", 'username',)

