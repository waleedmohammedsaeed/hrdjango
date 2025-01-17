from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages


def import_actions(request):
    if request.method == 'POST':
        try:
            call_command('actions')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('hr:employees')
    else:
        redirect('hr:employees')
    return render(request, 'homepage.html')


def import_area_side(request):
    if request.method == 'POST':
        try:
            call_command('areasides')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_eclass(request):
    if request.method == 'POST':
        try:
            call_command('eclass')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')


def import_general_specialization(request):
    if request.method == 'POST':
        try:
            call_command('general_sp')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_jobs(request):
    if request.method == 'POST':
        try:
            call_command('job')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_nationalities(request):
    if request.method == 'POST':
        try:
            call_command('nationality')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_specialization(request):
    if request.method == 'POST':
        try:
            call_command('rank')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

#----------------------------------------------------------------

def import_actual_work_side(request):
    if request.method == 'POST':
        try:
            call_command('actual_work_side')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')


def import_administrator(request):
    if request.method == 'POST':
        try:
            call_command('administrator')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_Job_owner(request):
    if request.method == 'POST':
        try:
            call_command('Job_owner')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

#----------------------------------------------------------------
def import_employees(request):
    if request.method == 'POST':
        try:
            call_command('emp')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')