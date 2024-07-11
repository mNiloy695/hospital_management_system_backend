from . import models
from rest_framework import serializers
class AppointmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Appointment
        fields='__all__'
    