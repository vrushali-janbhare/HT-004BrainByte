from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Doctor, Appointment

def book_appointment(request):

    doctors = Doctor.objects.all()

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile = request.POST.get("mobile")
        date = request.POST.get("date")
        doctor_id = request.POST.get("doctor")

        doctor = get_object_or_404(Doctor, id=doctor_id)

        count = Appointment.objects.filter(
            date=date,
            doctor=doctor,
            status="Waiting"
        ).count()

        token = f"A-{count + 1}"
        waiting_time = count * 10

        Appointment.objects.create(
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            date=date,
            doctor=doctor,
            token_number=token,
            status="Waiting"
        )

        return render(request, "book.html", {
            "doctors": doctors,
            "token": token,
            "waiting_time": waiting_time
        })

    return render(request, "book.html", {"doctors": doctors})


def mark_completed(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.status = "Completed"
    appointment.save()

    return HttpResponse(f"Appointment {id} Completed")

def home(request):
    return render(request, "home.html")

def reg(request):
    return render(request, "reg.html")

def user_login(request):
    return render(request, "login.html")

def doctor_panel(request):
    return render(request, "doctor_panel.html")