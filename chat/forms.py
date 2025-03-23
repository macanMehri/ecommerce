from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sent_text']
        widgets = {
            'sent_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 50}),
        }
