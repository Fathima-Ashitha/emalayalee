from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['first_name', 'last_name', 'whatsapp', 'location', 'username', 'password', 'email']
        help_texts = {
            'username': '',  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make these fields required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
    
    def clean_whatsapp(self):
        whatsapp = self.cleaned_data.get('whatsapp')
        if not whatsapp.isdigit() or len(whatsapp) != 10:
            raise ValidationError("WhatsApp number must be exactly 10 digits.")
        return whatsapp


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))