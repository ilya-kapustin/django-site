from django import forms
from django.http import request

from .models import *


class AddShop(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Не выбрана'

    class Meta:
        model = Shops
        fields = ['title', 'code_thing', 'img', 'description', 'price', 'group']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class AddGroup(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = ShopsGroup
        fields = ['name', 'description', 'img']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class AddComm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ShopsComm
        fields = ['author', 'grade', 'comm']
        widgets = {
            'comm': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }














