from django import forms
from .models import Message


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sent_text']
        widgets = {
            'sent_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
        }


class AdminMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['respond_text']
        widgets = {
            'respond_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
        }
