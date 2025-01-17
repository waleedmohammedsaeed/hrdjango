from django import forms
from .models import New_assignment
from hr.models import Employee
from django.forms.widgets import Select


class ReadOnlySelect(Select):
    def render(self, name, value, attrs=None, choices=()):
        attrs['disabled'] = 'disabled'  # Set the disabled attribute
        return super().render(name, value, attrs, choices)
class New_assignmentForm(forms.ModelForm):
    class Meta:
        model = New_assignment
        fields = ('employee', 'decision_no', 'decision_start_date', 'current_work', 'new_work', 'startwork', 'user', 'state')

        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control inputs'}),
            'decision_no': forms.TextInput(attrs={'class': 'form-control inputs'}),
            'decision_start_date' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control inputs'}),
            'current_work': forms.TextInput(attrs={'class': 'form-control inputs w-75', 'readonly': True}),
            'new_work' : forms.Select(attrs={'class': 'form-control inputs'}),
            'user': forms.HiddenInput(),
            'state': forms.HiddenInput(), #(attrs={'class': 'form-control inputs'}),
            'startwork': forms.DateInput(attrs={'type': 'date', 'class': 'form-control inputs'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     # Add a hidden field to store the value so it gets submitted
        #     self.fields['employee'] = forms.CharField(
        #         initial=self.instance.employee,
        #         widget=forms.HiddenInput()
        #     )

        def clean_employee(self):
            # Return the initial value since the field is read-only
            return self.instance.employee

    employee = ReadOnlySelect()
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.fields['employee'].disabled = True
        # self.fields['current_work'].disabled = True
        # self.fields['user'].disabled = True
