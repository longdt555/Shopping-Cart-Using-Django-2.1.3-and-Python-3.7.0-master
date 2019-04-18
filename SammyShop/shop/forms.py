#This form will authenticate the user with the data in the database
#Notice that we use the PasswordInput to render input element in HTML including type="password" attibute
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def cleaned_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password1 = self.cleaned_data['password1']
            if 'password' == 'password1' and password1:
                return password1
        raise forms.ValidationError('Password does not match.')

    def cleaned_user(self):
        if 'username' in self.cleaned_data:
            username = self.cleaned_data['username']
            if not re.search(r'^\w+$', username):
                raise forms.ValidationError('Username contains special characters.')
            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                return username
            raise forms.ValidationError('Username already exist.')

    def save(self):
        return User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'], email=self.cleaned_data['email'])
