from django.contrib import admin
from .models import New_assignment
# Register your models here.


# @admin.register(New_assignment)
# class New_assignment(admin.new_assignment):
#     list_display = ['decision_no', 'decision_start_date', 'current_work', 'new_work', 'user']

admin.site.register(New_assignment)