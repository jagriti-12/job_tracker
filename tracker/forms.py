from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
        widgets = {
            'date_applied': forms.DateInput(
                attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}
            ),
            'deadline': forms.DateInput(
                attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}
            ),
            'status': forms.Select(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
            'company': forms.TextInput(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
            'role': forms.TextInput(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
            'location': forms.TextInput(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
            'job_type': forms.TextInput(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
            'job_link': forms.URLInput(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
            'salary_range': forms.TextInput(
                attrs={'class': 'border rounded p-2 w-full'}
            ),
        }
