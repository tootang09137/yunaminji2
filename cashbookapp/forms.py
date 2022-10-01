from xml.dom import ValidationErr
from django import forms
from .models import Cashbook
from django.core.exceptions import ValidationError

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title', 'image', 'content']


    def __init__(self, *args, **kwargs):
        super(CashbookForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
    
    def __init__(self, *args, **kwargs):
        super(CashbookForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['content'].widget.attrs['readonly'] = True
