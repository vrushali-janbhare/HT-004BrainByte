from django.shortcuts import render
from .models import Doctor, Appointment

def home(request):
    return render(request, 'home.html')

def reg(request):
    return render(request, 'reg.html')

def book_appointment(request):

    doctors = Doctor.objects.all()

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile = request.POST.get("mobile")
        date = request.POST.get("date")
        doctor_id = request.POST.get("doctor")

        doctor = Doctor.objects.get(id=doctor_id)

        # Count today's appointments
        count = Appointment.objects.filter(date=date, doctor=doctor).count()

        token = f"A-{count + 1}"
        waiting_time = count * 10   # 10 mins per patient

        Appointment.objects.create(
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            date=date,
            doctor=doctor,
            token_number=token
        )

        return render(request, "book.html", {
            "doctors": doctors,
            "token": token,
            "waiting_time": waiting_time
        })

    return render(request, "book.html", {"doctors": doctors})





