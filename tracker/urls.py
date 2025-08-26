from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', views.job_list, name='job_list'),
    path('job/create/', views.job_create, name='job_create'),
    path('jobs/add/', views.job_create, name='job_create'),
    path('jobs/<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('', views.home, name='home'),
    path('add/', views.add_application, name='add_application'),
]
