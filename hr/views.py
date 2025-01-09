from sys import exception
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.forms import ValidationError
# from django.http import Http404, JsonResponse
from .models import Employee
from .forms import EmployeeForm
from django.core.exceptions import ObjectDoesNotExist



class Hr_main_view(ListView):
    model = Employee
    template_name = 'employees.html'
    context_object_name = 'employees'
    paginate_by = 10

def newemployee(request):
    eform = EmployeeForm()
    return render(request, 'newemployee.html', {'eform': eform})

def save_emp(request):
    if request.method == "POST":
        eform = EmployeeForm(request.POST)
        print(request.POST)
        print("request.POST")
        try:
            if eform.is_valid():
                eform.save()
                return redirect('hr:employees')
            else:
                print(eform.errors)
        except ValidationError as ve:
            raise exception.ValidationError
    return redirect('/')

def import_data(request):
    return render(request, 'command_store.html')

def getemployee(request):
    try:
        eno = request.POST.get('eno')
        emp =  get_object_or_404(Employee, empno=eno)
    except ObjectDoesNotExist:
        pass
    
    context = {'emp': emp}
    return render(request, 'employee.html', context)



