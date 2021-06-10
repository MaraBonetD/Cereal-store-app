from django.forms import ModelForm, widgets
from users.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        subscription_choices = [(True, 'Yes'), (False, 'No')]
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'telephone_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'is_subscribed': widgets.RadioSelect(choices=subscription_choices),
            'profile_picture': widgets.TextInput(attrs={'class': 'form-control'}),
        }
