from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Sandra', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Oyelaran',}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'you@example.com',}),
            'subject': forms.Select(attrs={'class': 'form-select',}),
            'message': forms.Textarea(attrs={'class': 'form-control','rows': 5,'placeholder': 'Tell me what you\'re looking for...',}),
        }