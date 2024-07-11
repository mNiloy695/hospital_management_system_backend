from django.contrib import admin
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

from .models import Appointment

class AppoinmentAdmin(admin.ModelAdmin):
    list_display=['appointment_types','appointment_status','symptom','time','cancel']

    # def doctor_name(self,obj):
    #     return obj.doctor.user.first_name
    
    # def paitent_name(self,obj):
    #     return obj.paitent.user.first_name
    
    def save_model(self,request,obj,form,change):
        print(obj.paitent.user.email)
        obj.save()
        if obj.appointment_status =='Running' and obj.appointment_types =='Online':
            email_subject="Your session is Running"
            email_body=render_to_string('admin_mail.html',{'user':obj.paitent.user,'doctor':obj.doctor})
            mail=EmailMultiAlternatives(email_subject,'',to=[obj.paitent.user.email])
            mail.attach_alternative(email_body,'text/html')
            print(obj.paitent.user.email)
            mail.send()
admin.site.register(Appointment,AppoinmentAdmin)