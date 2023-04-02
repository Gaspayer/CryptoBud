from django import forms
from .models import Project, CreatorProfile
from django.contrib.auth.forms import UserCreationForm

class CreatorProfileForm(forms.ModelForm):
    class Meta:
        model = CreatorProfile
        fields = ['bio', 'website', 'avatar']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'creator']
        widgets = {
            'creator': forms.HiddenInput()
        }
