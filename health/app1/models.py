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
