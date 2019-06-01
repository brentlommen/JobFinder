from django.urls import path
from . import views

urlpatterns = [
    path('<int:company_id>/', views.index, name='index'),
    path('<int:company_id>/addJob/<int:job_id>/', views.addJob, name='addJob'),
    path('<int:company_id>/activeJobs/', views.activeJobs, name='activeJobs'),
    path('<int:company_id>/activeJobs/removeJob/<int:job_id>/', views.removeJob, name='removeJob'),
    path('<int:company_id>/activeJobs/contact/<int:job_id>', views.contact, name='contact')
]