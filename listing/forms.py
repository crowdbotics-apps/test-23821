from django import forms
from listing.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'email', 'manufacture_year', 'postal_code', 'make', 'model', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'John@website.com'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'make': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'manufacture_year': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
