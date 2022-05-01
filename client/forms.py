from django import forms

class MessageForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()