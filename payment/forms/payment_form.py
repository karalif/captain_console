from django.forms import ModelForm, widgets
from payment.models import BillingInfo, PaymentInfo
from django import forms

class PaymentBillingForm(ModelForm):
    class Meta:
        model = BillingInfo
        exclude = {'id', 'user', 'active'}
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'checkbox'}),
            'country': widgets.Select(choices=[
                ('orange', 'Oranges'),
                ('banans', 'Bananas')
            ])
        }

class PaymentInfoForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = {'id', 'user', 'active'}
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'exp_month': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'exp_year': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'cvv': widgets.NumberInput(attrs={ 'class':'form-control' }),
        }


