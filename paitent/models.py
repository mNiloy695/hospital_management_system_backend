from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Paitent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='paitent/images')
    mobile_no=models.CharField(max_length=12)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
