from django import forms
# from .models import empno, ename, identifyno, jobtype, emptype, eclass, telNo, email, nationality, sex,bdate, job_title, rank, general_specialization, job_id, job_owner, owner_side, actual_work_area, actual_work_side, area_side_name, last_wag, attachment_date, hire_date, country_attachement_date, owner_status, end_service_date
from .models import Employee

class EmployeeForm(forms.ModelForm):


    class Meta:
        model = Employee
        # fields = ('empno', 'ename', 'identifyno', 'jobtype', 'emptype', 'eclass', 'telNo', 'email', 'nationality', 'sex','bdate', 'job_title', 'rank', 'general_specialization', 'job_id', 'job_owner', 'owner_side', 'actual_work_area', 'actual_work_side', 'area_side_name', 'last_wag', 'attachment_date', 'hire_date', 'country_attachement_date', 'owner_status', 'end_service_date')
        fields = ['emptype', 'jobtype', 'identity', 'eclass', 'empno', 'ename', 'telNo', 'email', 'nationality', 'sex', 'bdate', 'job_title', 'rank', 'general_specialization', 'job_id', 'job_owner', 'owner_side', 'actual_work_area', 'actual_work_side', 'area_side_type', 'adminstrator', 'lastAction_date', 'last_action', 'manager_name', 'hire_date', 'ministry_attachment', 'country_attachement_date', 'owner_status', 'service_type']
        # fields = '__all__'

        widgets = {
            'emptype': forms.Select(attrs={'class': ' form-select inputs'}),
            'jobtype': forms.Select(attrs={'class': 'inputs form-select'}),
            'identity': forms.TextInput(attrs={'class': 'inputs form-control', 'placeholder': "Identity Number"}),
            'eclass': forms.Select(attrs={'class': 'inputs form-select'}),
            'empno': forms.TextInput(attrs={'class': 'inputs form-control', 'placeholder': "Employee Number"}),
            'ename': forms.TextInput(attrs={'class': 'inputs form-control', 'placeholder': "Employee Name"}),
            'telNo': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Telephone Number"}),
            'email': forms.EmailInput(attrs={'class': 'form-control inputs', 'placeholder': "Email"}),
            'nationality': forms.Select(attrs={'class': 'form-control inputs'}),
            'sex': forms.Select(attrs={'class': 'form-select inputs'}),
            'bdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control inputs', 'placeholder': "Birth Date"}),
            'job_title': forms.Select(attrs={'class': 'form-select inputs'}),
            'rank': forms.Select(attrs={'class': 'form-select inputs'}),
            'general_specialization': forms.Select(attrs={'class': 'form-select inputs'}),
            'job_id': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Job ID"}),
            'job_owner': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Job Owner"}),
            'owner_side': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Owner Side"}),
            'actual_work_area': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Actual Work Area"}),
            'actual_work_side': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Actual Work Side"}),
            'area_side_type': forms.Select(attrs={'class': 'form-select inputs'}),
            'adminstrator': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Administrator"}),
            'lastAction_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control inputs', 'placeholder': "Last Action Date"}),
            'last_action': forms.Select(attrs={'class': 'form-select inputs'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Manager Name"}),
            'hire_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control inputs', 'placeholder': 'Hire Date'}),
            'ministry_attachment': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder':"ministry attachments"}),
            'country_attachement_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control inputs', 'placeholder': "Country Attachment Date"}),
            'owner_status': forms.TextInput(attrs={'class': 'form-control inputs', 'placeholder': "Owner Status"}),
            'service_type': forms.NumberInput(attrs={'class': 'form-control inputs', 'placeholder': "Service Type"}),
        }
