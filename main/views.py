from django.shortcuts import render
from django.db.models import Count
from hr.models import Eclass, Employee, Nationality
# from .account.models import CustomUser

 #Create your views here.
def main(request):
    return render(request, 'mainpage.html')

def hr(request):
    return render(request, 'hr.html')

def payroll(request):
    return render(request, 'payroll.html')

def assignment(request):
    sa = Employee.objects.filter(nationality=4).aggregate(totals=Count('nationality'))
    em = Employee.objects.values('eclass__className').annotate(totals=Count('eclass'))
    na = Employee.objects.values('nationality__nationality_name').annotate(total=Count('nationality'))
    context={
        'em': em,
        'na': na,
        'sa': sa,
    }
    return render(request, 'assignment.html', context)

def jobs(request):
    return render(request, 'jobs.html')

def recruitment(request):
    return render(request, 'recruitment.html')

def usersmanagement(request):
    return render(request, 'usersmanagement.html')

def newassignment(request):
    return render(request, "assign/newassignment.html")
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
