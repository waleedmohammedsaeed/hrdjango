from django.urls import path

from hr.urls import app_name
from . import views

app_name = "accounts"

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('deactivate/', views.deactivate_user, name='deactivate_user'),
    path('register_user/', views.register_user, name='register_user'),
    # path('creation-user/', views.creation_user, name='creation_user'),

]
