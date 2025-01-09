from django.urls import path
from .views import Hr_main_view
from . import views
from . import viewsimportdata

app_name = "hr"

urlpatterns = [
    path('employees/', Hr_main_view.as_view(), name="employees"),
    path('newemployee', views.newemployee, name="newemployee"),
    path('save_emp', views.save_emp, name="save_emp"),
    path('getemployee/', views.getemployee, name="getemployee"),

    path('import_data/', views.import_data, name="import_data"),
    path('import_actions', viewsimportdata.import_actions, name='import_actions'),
    path('import_area_side', viewsimportdata.import_area_side, name='import_area_side'),
    path('import_area_side', viewsimportdata.import_area_side, name='import_area_side'),
    path('import_eclass', viewsimportdata.import_eclass, name='import_eclass'),
    path('import_general_specialization', viewsimportdata.import_general_specialization, name='import_general_specialization'),
    path('import_jobs', viewsimportdata.import_jobs, name='import_jobs'),
    path('import_nationalities', viewsimportdata.import_nationalities, name='import_nationalities'),
    path('import_specialization', viewsimportdata.import_specialization, name='import_specialization'),

    path('import_employees', viewsimportdata.import_employees, name='import_employees'),
]
