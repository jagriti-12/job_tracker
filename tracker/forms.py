# tracker/forms.py
from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'role', 'application_date', 'status']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[
                ('Applied', 'Applied'),
                ('Interview', 'Interview'),
                ('Offer', 'Offer'),
                ('Rejected', 'Rejected'),
            ])
        }
