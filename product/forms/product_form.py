from django.forms import ModelForm, widgets
from product.models import Product, ProductImage
from django import forms




class ProductUpdateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.Select(attrs={ 'class':'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'console': widgets.Select(attrs={ 'class':'form-control' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class':'checkbox' })

        }

class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model= Product
        exclude = {'id'}
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.Select(attrs={ 'class':'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class':'form-control' }),
            'console': widgets.Select(attrs={ 'class':'form-control' }),
            'on_sale': widgets.CheckboxInput(attrs={ 'class':'checkbox' })
        }
