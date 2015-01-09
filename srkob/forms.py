# -*- coding: utf-8 -*-
from srkob.models import Profile
from django.contrib.auth.models import User
from django import forms

#formularz z modelu User
class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Podaj nazwę użytkownika:")
    email = forms.CharField(help_text="Podaj email:")
    password = forms.CharField('Hasło', widget=forms.PasswordInput(), help_text="Podaj hasło:")
    first_name = forms.CharField(help_text="Podaj imię:")
    last_name = forms.CharField(help_text="Podaj nazwisko:")
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

#formularz z modelu Profile
class ProfileForm(forms.ModelForm):
    p_number = forms.IntegerField(help_text="Podaj numer pesel:")
    street = forms.CharField(help_text="Podaj ulicę:")
    nr_house = forms.IntegerField(help_text="Podaj numer domu:")
    nr_flat = forms.IntegerField(help_text="*Podaj numer mieszkania:", required=False)
    post_code = forms.CharField(help_text="Podaj kod pocztowy:")
    city = forms.CharField(help_text="Podaj nazwe miejscowości:")

    
    class Meta:
        model = Profile
        fields = ('p_number', 'street', 'nr_house', 'nr_flat', 'post_code', 'city')

