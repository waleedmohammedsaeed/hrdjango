from django.shortcuts import render
# from .account.models import CustomUser

 #Create your views here.
def main(request):
    # userr = CustomUser.objects.get(username=request.user)
    return render(request, 'mainpage.html')

def hr(request):
    return render(request, 'hr.html')

def payroll(request):
    return render(request, 'payroll.html')

def assignment(request):
    return render(request, 'assignment.html')

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
