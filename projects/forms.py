from django import forms
from .models import Project, Task
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator
import re

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = [
            'name', 
            'description', 
            'start_date', 
            'end_date', 
            'budget', 
            'status', 
            'owner', 
            'owner_email'
        ]

    name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter the name of the project (max 100 characters).',
        error_messages={
            'required': 'The project name is required.',
            'max_length': 'The project name cannot exceed 100 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Project Name'})
    )
    
    description = forms.CharField(
        max_length=800,
        widget=forms.Textarea(attrs={'placeholder': 'Project Description'}),
        required=True,
        help_text='Enter the description of the project.',
        error_messages={
            'required': 'The project description is required.',
            'max_length': 'The description cannot exceed 800 characters.'
        }
    )
    
    start_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Enter start date', 'class': 'form-control datepicker','type': 'date',}),
        help_text='Enter the start date of the project.',
        error_messages={
            'required': 'The start date is required.',
            'invalid': 'Enter a valid date.'
        }
    )
    
    end_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Enter end date', 'class': 'form-control datepicker','type': 'date',}),
        help_text='Enter the end date of the project.',
        error_messages={
            'required': 'The end date is required.',
            'invalid': 'Enter a valid date.'
        }
    )
    
    budget = forms.DecimalField(
        min_value=0,
        max_digits=10,
        decimal_places=2,
        required=True,
        help_text='Enter the budget for the project.',
        error_messages={
            'required': 'The budget is required.',
            'invalid': 'Enter a valid decimal number.',
            'min_value': 'The budget cannot be a negative number.',
            'max_digits': 'The budget cannot have more than 10 digits in total.',
            'max_decimal_places': 'The budget cannot have more than 2 decimal places.'
        },
        widget=forms.NumberInput(attrs={'placeholder': 'Budget'})
    )
    
    status = forms.ChoiceField(
        choices=[
            ('Not Started', 'Not Started'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed')
        ],
        required=True,
        help_text='Select the status of the project.',
        error_messages={
            'required': 'The status is required.'
        },
        widget=forms.Select(attrs={'placeholder': 'Select status'})
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
        # validators=[EmailValidator('Enter a valid email address.')],
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
        description = cleaned_data.get("description")
        budget = cleaned_data.get("budget")
        owner = cleaned_data.get("owner")
        owner_email = cleaned_data.get("owner_email")
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        
        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("End date should be greater than start date.")
            
        # if not self.is_valid_email(owner_email):
        #     self.add_error('owner_email', 'Enter a valid email address.')
        
        return cleaned_data
        
        

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'project',
            'title', 
            'description', 
            'due_date', 
            'priority', 
            'completed'
        ]

    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        required=True,
        help_text='Select the project for this task.',
        error_messages={
            'required': 'The project is required.'
        },
        widget=forms.Select(attrs={'placeholder': 'Select Project'})
    )

    title = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter the title of the task (max 100 characters).',
        error_messages={
            'required': 'The task title is required.',
            'max_length': 'The task title cannot exceed 100 characters.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Task Title'})
    )

    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Task Description'}),
        required=True,
        help_text='Enter the description of the task.',
        error_messages={
            'required': 'The description is required.',
            'max_length': 'The description cannot exceed 1000 characters.'
        }
    )

    due_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Enter due date', 'class': 'form-control datepicker', 'type': 'date'}),
        help_text='Enter the due date of the task.',
        error_messages={
            'required': 'The due date is required.',
            'invalid': 'Enter a valid date.'
        }
    )

    priority = forms.ChoiceField(
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High')
        ],
        required=True,
        help_text='Select the priority of the task.',
        error_messages={
            'required': 'The priority is required.'
        },
        widget=forms.Select(attrs={'placeholder': 'Select Priority'})
    )

    completed = forms.BooleanField(
        required=False,
        initial=False,
        help_text='Mark as completed.',
        widget=forms.CheckboxInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        due_date = cleaned_data.get("due_date")
        priority = cleaned_data.get("priority")
        completed = cleaned_data.get("completed")
        project = cleaned_data.get("project")

        # Add any additional validation logic here

        return cleaned_data
