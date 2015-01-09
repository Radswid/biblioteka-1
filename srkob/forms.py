from rango.models import Profile
from django.contrib.auth.models import User
from django import forms

class UserForm(form.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class ProfileForm(forms.ModelForms):
    class Meta:
        model = Profile
        fields = ('p_number', 'street', 'nr_house', 'nr_flat', 'post_code', 'city')
