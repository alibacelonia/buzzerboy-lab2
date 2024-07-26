from django import forms
from .models import Country, State
from django.core.validators import RegexValidator, EmailValidator
import re

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = [
            'name', 
            'code', 
            'population', 
            'description', 
            'independence_day', 
            'currency', 
            'continent', 
            'owner', 
            'owner_email'
        ]

    name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter the name of the country (max 100 characters).',
        error_messages={
            'required': 'The country name is required.',
            'max_length': 'The country name cannot exceed 100 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Country Name'})
    )

    code = forms.CharField(
        max_length=10,
        required=True,
        help_text='Enter the country code (max 10 characters).',
        error_messages={
            'required': 'The country code is required.',
            'max_length': 'The country code cannot exceed 10 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Country Code'})
    )

    population = forms.IntegerField(
        required=True,
        min_value=0,
        help_text='Enter the population of the country.',
        error_messages={
            'required': 'The population is required.',
            'invalid': 'Enter a valid integer.',
            'min_value': 'The population cannot be negative.'
        },
        widget=forms.NumberInput(attrs={'placeholder': 'Population'})
    )

    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Country Description'}),
        required=True,
        help_text='Enter the description of the country.',
        error_messages={
            'required': 'The description is required.',
            'max_length': 'The description cannot exceed 1000 characters.'
        }
    )

    independence_day = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Enter independence day', 'class': 'form-control datepicker','type': 'date',}),
        help_text='Enter the independence day of the country.',
        error_messages={
            'required': 'The independence day is required.',
            'invalid': 'Enter a valid date.'
        }
    )

    currency = forms.CharField(
        max_length=50,
        required=True,
        help_text='Enter the currency of the country (max 50 characters).',
        error_messages={
            'required': 'The currency is required.',
            'max_length': 'The currency cannot exceed 50 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Currency'})
    )

    continent = forms.ChoiceField(
        choices=[
            ('Africa', 'Africa'),
            ('Asia', 'Asia'),
            ('Europe', 'Europe'),
            ('North America', 'North America'),
            ('South America', 'South America'),
            ('Oceania', 'Oceania'),
            ('Antarctica', 'Antarctica')
        ],
        required=True,
        help_text='Select the continent of the country.',
        error_messages={
            'required': 'The continent is required.'
        },
        widget=forms.Select(attrs={'placeholder': 'Select continent'})
    )

    owner = forms.CharField(
        max_length=100,
        required=True,
        validators=[RegexValidator(regex='^[a-zA-Z\s]*$', message='Owner name should only contain letters and spaces.')],
        help_text='Enter the name of the owner (max 100 characters, letters and spaces only).',
        error_messages={
            'max_length': 'The owner name cannot exceed 100 characters.',
            'invalid': 'Owner name should only contain letters and spaces.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Owner Name'})
    )

    owner_email = forms.EmailField(
        required=True,
        max_length=100,
        error_messages={
            'max_length': 'Email address cannot exceed 100 characters.',
            'invalid': 'Enter a valid email address.'
        },
        widget=forms.EmailInput(attrs={'placeholder': 'Owner Email', "type": 'email'})
    )

    def is_valid_email(self, email):
        if email is None:
            return False
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        code = cleaned_data.get("code")
        population = cleaned_data.get("population")
        description = cleaned_data.get("description")
        independence_day = cleaned_data.get("independence_day")
        currency = cleaned_data.get("currency")
        continent = cleaned_data.get("continent")
        owner = cleaned_data.get("owner")
        owner_email = cleaned_data.get("owner_email")
        
        # Add any additional validation logic here
        
        return cleaned_data

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = [
            'country',
            'name', 
            'code', 
            'population', 
            'description', 
            'established_date'
        ]

    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        required=True,
        help_text='Select the country for this state.',
        error_messages={
            'required': 'The country is required.'
        },
        widget=forms.Select(attrs={'placeholder': 'Select Country'})
    )

    name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter the name of the state (max 100 characters).',
        error_messages={
            'required': 'The state name is required.',
            'max_length': 'The state name cannot exceed 100 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'State Name'})
    )

    code = forms.CharField(
        max_length=10,
        required=True,
        help_text='Enter the state code (max 10 characters).',
        error_messages={
            'required': 'The state code is required.',
            'max_length': 'The state code cannot exceed 10 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'State Code'})
    )

    population = forms.IntegerField(
        required=True,
        min_value=0,
        help_text='Enter the population of the state.',
        error_messages={
            'required': 'The population is required.',
            'invalid': 'Enter a valid integer.',
            'min_value': 'The population cannot be negative.'
        },
        widget=forms.NumberInput(attrs={'placeholder': 'Population'})
    )

    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'State Description'}),
        required=True,
        help_text='Enter the description of the state.',
        error_messages={
            'required': 'The description is required.',
            'max_length': 'The description cannot exceed 1000 characters.'
        }
    )

    established_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Enter established date', 'class': 'form-control datepicker', 'type': 'date'}),
        help_text='Enter the established date of the state.',
        error_messages={
            'required': 'The established date is required.',
            'invalid': 'Enter a valid date.'
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        code = cleaned_data.get("code")
        population = cleaned_data.get("population")
        description = cleaned_data.get("description")
        established_date = cleaned_data.get("established_date")
        country = cleaned_data.get("country")

        # Add any additional validation logic here

        return cleaned_data

