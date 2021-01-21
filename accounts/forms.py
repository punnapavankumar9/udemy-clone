from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, ProfileLinks

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('professional_headline', 'professional_info',)
        labels = {
            "professional_headline": "profile headline",
            "professional_info": "Professional info"
        }

class ProfileLinksForm(forms.ModelForm):
    class Meta:
        model = ProfileLinks
        fields = ('website', 'facebook','twitter', 'github', 'linkedin')