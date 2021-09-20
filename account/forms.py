from django import forms
from . models import Profile

class Profile_Model_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
