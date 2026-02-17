from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.specialization}"


class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    token_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.token_number}"
