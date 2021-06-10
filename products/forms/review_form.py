from django.forms import ModelForm, widgets
from django import forms
from products.models import Product,ProductReview

class AddReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        exclude = ['id', 'user', 'product', 'timestamp']
        widgets = {
            'text': widgets.TextInput(attrs={'class':'form-control'}),
            'rating': widgets.TextInput(attrs={'class':'form-control'}),
        }