from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={'style': 'background: rgba(255,255,255,0.05); border: none; color: rgba(255,255,255,0.7);'})
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'background: rgba(255,255,255,0.05); border: none; color: rgba(255,255,255,0.7);',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'style': 'background: rgba(255,255,255,0.05); border: none; color: rgba(255,255,255,0.7);',
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'style': 'background: rgba(255,255,255,0.05); border: none; color: rgba(255,255,255,0.7);',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={'style': 'background: rgba(255,255,255,0.05); border: none; color: rgba(255,255,255,0.7);'})
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'background: rgba(255,255,255,0.05); border: none; color: rgba(255,255,255,0.7);',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
