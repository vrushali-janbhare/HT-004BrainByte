from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reg(request):
    return render(request, 'reg.html')


    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')




    from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



    from django.contrib.admin.views.decorators import staff_member_required
from .models import Appointment

@staff_member_required
def doctor_panel(request):

    appointments = Appointment.objects.filter(status='Waiting').order_by('queue_number')

    return render(request, 'doctor_panel.html', {'appointments': appointments})


@staff_member_required
def mark_completed(request, id):
    appt = Appointment.objects.get(id=id)
    appt.status = "Completed"
    appt.save()
    return redirect('doctor_panel')



@staff_member_required
def skip_patient(request, id):
    appt = Appointment.objects.get(id=id)
    appt.status = "Skipped"
    appt.save()
    return redirect('doctor_panel')



@staff_member_required
def emergency_patient(request, id):
    appt = Appointment.objects.get(id=id)
    appt.queue_number = 1
    appt.status = "Emergency"
    appt.save()
    return redirect('doctor_panel')





