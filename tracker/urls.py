from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),         # Dashboard
    path('jobs/', views.job_list, name='job_list'),      # Jobs List
    path('jobs/add/', views.job_create, name='job_create'),  # Add Job
    path('jobs/<int:pk>/edit/', views.job_edit, name='job_edit'),  # Edit Job
    path('jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),  # Delete Job

    # agar alag home page rakhna hai dashboard se
    path('home/', views.home, name='home'),              

    # alternate add_application agar chahiye
    path('add/', views.add_application, name='add_application'),
]
