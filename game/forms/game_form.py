from django.forms import ModelForm, widgets
from game.models import Games
from django import forms

class GameUpdateForm(ModelForm):
    class Meta:
        model= Games
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.Select(attrs={ 'class':'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'console': widgets.Select(attrs={ 'class':'form-control' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class':'checkbox' })
        }

class GameCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model= Games
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.Select(attrs={ 'class':'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'console': widgets.Select(attrs={ 'class':'form-control' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class':'checkbox' })
        }
