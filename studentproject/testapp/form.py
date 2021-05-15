from testapp.models import student
from django import forms
from django.core import validators
class updateForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
