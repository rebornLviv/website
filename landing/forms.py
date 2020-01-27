from django import forms
from django.forms import TextInput

from .models import *

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        #fields = [""]
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget = TextInput(attrs={
            'class': 'widtharea',
            'name': 'author',
            'placeholder': 'Tell Us Couple Words About Your Project'})
        self.fields['phone'].widget = TextInput(attrs={
            'class': 'widthinput',
            'name': 'author',
            'placeholder': 'Your Phone'})
        self.fields['name'].widget = TextInput(attrs={
            'class': 'gtw-inline',
            'name': 'author',
            'placeholder': "Your Name"})
        self.fields['email'].widget = TextInput(attrs={
            'class': 'gtw-inline',
            'name': 'author',
            'placeholder': "Your Email"})
