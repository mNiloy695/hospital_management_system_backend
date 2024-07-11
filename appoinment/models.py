from django.db import models

# Create your models here.
from paitent.models import Paitent
from doctor.models import Doctor,AvailableTime


APPOINTMENT_TYPES=[
    ('Pending','Pending'),
    ('Running','Running'),
    ('Completed','Completed'),
]

APPOINTMENT_STATUS=[
    ('Online','Online'),
    ('Offline','Offline'),
]
class Appointment(models.Model):
    paitent=models.ForeignKey(Paitent,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_types=models.CharField(max_length=20,choices=APPOINTMENT_TYPES,default="Pending")
    appointment_status=models.CharField(max_length=20,choices=APPOINTMENT_STATUS)
    symptom=models.TextField()
    time=models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

   
    def __str__(self):
        return f"{self.paitent.user.first_name} {self.doctor.user.first_name}"