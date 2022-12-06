from django.forms import ModelForm
from django import forms
from login.models import Customer

class FormCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput ({'class': 'form-control'}),
            'email' : forms.TextInput ({'class': 'form-control'}),
            'alamat' : forms.TextInput ({'class': 'form-control'}),
        }