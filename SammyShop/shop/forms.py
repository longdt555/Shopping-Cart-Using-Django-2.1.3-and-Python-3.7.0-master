#This form will authenticate the user with the data in the database
#Notice that we use the PasswordInput to render input element in HTML including type="password" attibute
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
