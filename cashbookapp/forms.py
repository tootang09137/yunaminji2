from xml.dom import ValidationErr
from django import forms
from .models import Cashbook
from django.core.exceptions import ValidationError

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title', 'content', 'image']
