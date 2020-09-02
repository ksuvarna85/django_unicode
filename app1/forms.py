from django import forms
from app1.models import User,Student,Teacher

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=Student
        fields=('sap_id','year','division')

class UserProfileTeacherInfoForm(forms.ModelForm):
    class Meta():
        model=Teacher
        fields=('qualification',)
