from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeType

TYPES = [('manager', 'Manager'), ('computers', 'Computers')]


class SignUpForm(UserCreationForm):
    employeeFirst = forms.CharField(label='First Name', max_length=25)
    employeeLast = forms.CharField(label='Last Name', max_length=25)
    employeeId = forms.CharField(label='Employee ID', max_length=8)
    employeeType = forms.CharField(label='Employee Type', widget=forms.Select(choices=TYPES))

    class Meta:
        model = User
        fields = ('employeeFirst', 'employeeLast', 'employeeId', 'employeeType', 'password1', 'password2', )


class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['type']

