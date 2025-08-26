from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company', 'role', 'location', 'job_type',
            'date_applied', 'deadline', 'status',
            'salary_range', 'job_link'
        ]
        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-2',
                'placeholder': 'Enter company name'
            }),
            'role': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-2',
                'placeholder': 'Enter role'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-2',
                'placeholder': 'Enter location'
            }),
            'job_type': forms.Select(attrs={
                'class': 'w-full border rounded-lg p-2'
            }),
            'date_applied': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border rounded-lg p-2'
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border rounded-lg p-2'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full border rounded-lg p-2'
            }),
            'salary_range': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-2',
                'placeholder': 'Optional'
            }),
            'job_link': forms.URLInput(attrs={
                'class': 'w-full border rounded-lg p-2',
                'placeholder': 'https://example.com/job'
            }),
        }

    # Optional: clean job_link (extra validation)
    def clean_job_link(self):
        job_link = self.cleaned_data.get('job_link')
        if job_link and not job_link.startswith(('http://', 'https://')):
            raise forms.ValidationError("Job link must start with http:// or https://")
        return job_link
