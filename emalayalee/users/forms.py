from django import forms
from .models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['name', 'whatsapp', 'location', 'username', 'email']
    
    def clean_whatsapp(self):
        whatsapp = self.cleaned_data.get('whatsapp')
        if not whatsapp.isdigit() or len(whatsapp) != 10:
            raise ValidationError("WhatsApp number must be exactly 10 digits.")
        return whatsapp