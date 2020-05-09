from django.forms import ModelForm, widgets
from console.models import Console
from django import forms

class ConsoleUpdateForm(ModelForm):
    class Meta:
        model= Console
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.Select(attrs={ 'class':'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'console': widgets.Select(attrs={ 'class':'form-control' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class':'checkbox' })
        }


class ConsoleCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model= Console
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.Select(attrs={ 'class':'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'console': widgets.Select(attrs={ 'class':'form-control' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class':'checkbox' })
        }
