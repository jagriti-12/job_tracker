from django.shortcuts import render, get_object_or_404, redirect
from .models import JobApplication
from django.utils import timezone
from django import forms
from .forms import JobApplicationForm

# Simple form for jobs
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'

# Dashboard view
def dashboard(request):
    jobs = JobApplication.objects.all()
    total = jobs.count()
    applied = jobs.filter(status="applied").count()
    interview = jobs.filter(status="interview").count()
    rejected = jobs.filter(status="rejected").count()
    selected = jobs.filter(status="selected").count()

    context = {
        'total': total,
        'applied': applied,
        'interview': interview,
        'rejected': rejected,
        'selected': selected,
    }
    return render(request, 'tracker/dashboard.html', context)

# List all jobs
def job_list(request):
    jobs = JobApplication.objects.all().order_by('-date_applied') #Newest First
    return render(request, 'tracker/job_list.html', {'jobs': jobs})

# Add new job
def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
        else:
            print("Form Errors:", form.errors)
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/job_form.html', {'form': form})


# Edit job
def job_edit(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'tracker/job_form.html', {'form': form})

# Delete job
def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'tracker/job_confirm_delete.html', {'job': job})

# tracker/views.py
def home(request):
    applications = JobApplication.objects.all().order_by('-application_date')
    return render(request, 'tracker/home.html', {'applications': applications})

def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/add_application.html', {'form': form})
