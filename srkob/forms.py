# -*- coding: utf-8 -*-
from srkob.models import Profile
from django.contrib.auth.models import User
from django import forms

#formularz z modelu User
class UserForm(forms.ModelForm):
    password = forms.CharField('Hasło', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

#formularz z modelu Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('p_number', 'street', 'nr_house', 'nr_flat', 'post_code', 'city')

