from django.shortcuts import render, redirect
from .forms import New_assignmentForm
from hr.models import Employee
from .models import New_assignment
from django.db.models import Q, Count

# Create your views here.

def assignment_main_page(request):
    ass = New_assignment.objects.filter(state=1)
    return render(request, 'assignment_main_page.html', {'ass': ass})

def assignment_main_hr_manager(request):
    selected = Q(state=1)|Q(state=2)
    nass = New_assignment.objects.filter(selected)
    context={'nass': nass}
    return render(request, 'assignment_main_hr_manager.html', context)


def save_assignment(request):
    if request.method == 'POST':
        f = New_assignmentForm(request.POST)

        if f.is_valid():
            f.save()
            return redirect('/')
        else:
            print(f.errors)
    return render(request, 'assignment_main_page.html')

def newassignment(request):
    if request.method == 'POST':
        n = request.POST.get('num')
        e = Employee.objects.get(empno=n)
        initial_data = {
            'employee': e, 
            'current_work': e.actual_work_side,
            'user': request.user   
        }
        form = New_assignmentForm(initial=initial_data)
        return render(request, 'new-assignment.html', {'assignmentform': form})
    return render(request, 'newass_request.html')

def approved(request):
    if request.method == 'POST':
        # approved_items = request.POST.get('appr')
        # for approved, value in request.POST.items():
        #     print(f' items selected are {approved}={value}')

        ns = request.POST.getlist('approved_req')
        newass = New_assignment.objects.filter(id__in=ns)
        for nn in newass:
            if nn.state == 1:
                nn.state = 2
        New_assignment.objects.bulk_update(newass, ['state'])

        return redirect('/')
    else:
        return redirect('assignment_main_hr_manager')