from django.forms import ModelForm, ValidationError
from .models import Client


class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email']

    def clean_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise ValidationError('adsadadadad')
        return phone_number
