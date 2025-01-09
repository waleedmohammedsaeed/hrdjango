from django.contrib import admin
from .models import Eclass, Nationality, Job, Specialization, GeneralSpecialization, Area_side, Actions, Employee

# Register your models here.

admin.site.register(Eclass)
admin.site.register(Nationality)
admin.site.register(Job)
admin.site.register(Specialization)
admin.site.register(GeneralSpecialization)
admin.site.register(Area_side)
admin.site.register(Actions)
# admin.site.register(Employee)

@admin.register(Employee)
class EmployrrModelAdmin(admin.ModelAdmin):
    list_display = ('empno', 'ename', 'nationality', 'general_specialization', 'actual_work_area',)
    list_filter = ('nationality', 'eclass',)