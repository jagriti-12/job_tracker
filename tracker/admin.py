from django.contrib import admin

# Register your models here.
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'status', 'date_applied', 'source')
    list_filter = ('status', 'source', 'job_type')
    search_fields = ('company', 'role', 'notes')

# 👉 This tells Django: (For line 6 - 10)
# Show JobApplication in the admin.
# Display those fields in a table view.
# Add filters (by status, source, job type).
# Add a search box (company, role, notes).