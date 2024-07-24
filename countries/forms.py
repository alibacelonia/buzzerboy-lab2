from django import forms
from .models import Country, State

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'independence_day': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Select Independence Day', 'type': 'date'}),
            'population': forms.NumberInput(attrs={'min': 0, 'step': 1, 'placeholder': 'Enter population'}),
        }

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'
        widgets = {
            'established_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Select Established Date', 'type': 'date'}),
            'population': forms.NumberInput(attrs={'min': 0, 'step': 1, 'placeholder': 'Enter population'}),
        }
