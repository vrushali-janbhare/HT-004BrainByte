from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    queue_number = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Waiting')

    def __str__(self):
        return self.patient.username


from django.utils import timezone

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    queue_number = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Waiting')

    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.patient.username
