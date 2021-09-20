from django import forms
from . models import Profile, Account

# class Profile_Model_Form(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['age', 'image_file', 'name']
#         widgets = {
#             'age': forms.EmailInput(attrs={"class": "form-control"}),
#         }


class Account_creation_Model_Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name']
        labels = {'account_name': 'Имя счета:'}
        widgets = {
            'account_name': forms.TextInput(attrs={"class": "form-control"}),
        }
       

class Account_add_money_Model_Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['money']
        labels = {'money': 'Сколько денег добавить:'}
        widgets = {
            'money': forms.NumberInput(attrs={"class": "form-control", "step": 0.01}),
        }
