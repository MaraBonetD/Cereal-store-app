from django.forms import ModelForm, widgets
from django import forms
from products.models import Product,Ingredient

class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class':'form-control'}),
            'brand': widgets.TextInput(attrs={'class':'form-control'}),
            'price': widgets.NumberInput(attrs={'class':'form-control'}),
            'description': widgets.TextInput(attrs={'class':'form-control'}),
            'category': widgets.Select(attrs={'class':'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class':'checkbox block'})
        }

class ProductUpdateForm(ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class':'form-control'}),
            'brand': widgets.TextInput(attrs={'class':'form-control'}),
            'price': widgets.NumberInput(attrs={'class':'form-control'}),
            'description': widgets.TextInput(attrs={'class':'form-control'}),
            'category': widgets.Select(attrs={'class':'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class':'checkbox block'})
        }