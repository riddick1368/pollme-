from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import redirect




class user_registration_form(forms.Form):
    Username = forms.CharField(label="Username",max_length=100,min_length=5 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password1 = forms.CharField(label="Password", max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Password2 = forms.CharField(label="Confirm Password", max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))



    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('Password1')
        p2 = cleaned_data.get('Password2')
        if not p2:
            raise forms.ValidationError("You must confirm your password")
        if p1 != p2:
            raise forms.ValidationError("Your passwords do not match")
        return p2





    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError("email already exists!")
        return email









