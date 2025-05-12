from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount', 'payment_method', 'donation_type', 'message', 'is_anonymous']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount', 'min': '1', 'step': '0.01'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'donation_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional message', 'rows': 4}),
            'is_anonymous': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError('Donation amount must be greater than 0')
        return amount

class AdoptionForm(forms.Form):
   pet_name = forms.CharField(max_length=100)
   adopter_name = forms.CharField(max_length=100)
   adopter_email = forms.EmailField()
   adoption_message = forms.CharField(widget=forms.Textarea, required=False)