from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

# Forms---------------
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confrom Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        labels ={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = { 
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class loginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password=forms.CharField(label=_('password'), strip='Flase',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))