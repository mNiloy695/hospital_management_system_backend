from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from . serializers import AppointmentModelSerializer

from .models import Appointment
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentModelSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        paitent_id=self.request.query_params.get('paitent_id')
        if paitent_id:
            queryset=queryset.filter(paitent_id=paitent_id)
        return queryset
        