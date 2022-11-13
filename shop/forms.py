from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['name', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
        # exclude = ['']
