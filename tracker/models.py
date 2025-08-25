from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('selected', 'Selected'),
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)  # e.g., Full-time, Internship
    date_applied = models.DateField()
    job_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)  # LinkedIn, Indeed, etc.
    deadline = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company} - {self.role} ({self.status})"
