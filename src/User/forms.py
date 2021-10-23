from django import forms


class SigninForm(forms.Form):
    email = forms.EmailField(max_length=45, required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=45, required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    cgu_accept = forms.BooleanField(initial=True)