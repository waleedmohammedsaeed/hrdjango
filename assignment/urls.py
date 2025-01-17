from django.urls import path
from . import views

app_name = 'assignment'

urlpatterns = [
    path('', views.assignment_main_page, name='assignment'),
    path('new-assignment', views.newassignment, name='newassignment'),
    path('assignment-approvement', views.assignment_main_hr_manager, name='assignment_main_hr_manager'),
    path('save_assignment', views.save_assignment, name='save_assignment'),
    path('approved', views.approved, name='approved'),

]
