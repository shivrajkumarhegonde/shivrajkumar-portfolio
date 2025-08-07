# core/forms.py
from django import forms

class ContactForm(forms.Form):
    """
    A form for users to send a message from the contact page.
    """
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'class': 'form-input'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-input'
    }))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'class': 'form-input'
    }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'placeholder': 'Your Message',
        'class': 'form-input'
    }))