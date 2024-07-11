from django.db import models
from django.contrib.auth.models import User
from paitent.models import Paitent
from datetime import datetime
# Create your models here.
class Specialization(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    
class AvailableTime(models.Model):
    time=models.CharField(max_length=100)

    def __str__(self):
        return self.time

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    designation=models.ManyToManyField(Designation)
    specialization=models.ManyToManyField(Specialization)
    availabletime=models.ManyToManyField(AvailableTime)
    meet_link=models.CharField(max_length=100)
    image=models.ImageField(upload_to="doctor/images")
    fee=models.IntegerField()

    def __str__(self):
        return f'{self.user.first_name}  {self.user.last_name}'

STAR_CHOICE={
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
}
class Review(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    reviewer=models.ForeignKey(Paitent,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=datetime.now())
    rating=models.CharField(max_length=20,choices=STAR_CHOICE)
    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name} {self.doctor.user.first_name} Paitent: {self.reviewer.user.first_name} {self.reviewer.user.last_name}"