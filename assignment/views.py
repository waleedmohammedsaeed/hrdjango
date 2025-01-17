from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
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
        try:
            e = get_object_or_404(Employee, empno=n)
        except Http404:
            return render(request, 'page404.html')
        
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

        dec = request.POST.get('appr')
        ns = request.POST.getlist('approved_req')
        newass = New_assignment.objects.filter(id__in=ns)
        print(dec)
        for nn in newass:
            if nn.state == 1:
               nn.state = dec
            
        New_assignment.objects.bulk_update(newass, ['state'])

        return redirect('/')
    else:
        return redirect('assignment_main_hr_manager')
    
def oneassignedinfo(request, id):
    one = get_object_or_404(New_assignment, id=id)
    return render(request, 'one_assigned_info.html', {'one': one})