from audioop import maxpp
from email.policy import default
from django import forms


class DetailForm(forms.Form):
    pieces = forms.IntegerField(label='数量')