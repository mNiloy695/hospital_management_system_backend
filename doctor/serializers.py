from . import models
from rest_framework import serializers
class DoctorModelSerializer(serializers.ModelSerializer):
    specialization=serializers.StringRelatedField(many=True)
    designation=serializers.StringRelatedField(many=True)
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Doctor
        fields='__all__'

class SpecializatinModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Specialization
        fields='__all__'

class DesignationModelSerializer(serializers.ModelSerializer):
    class Meta: 
        model=models.Designation
        fields="__all__"

class AvailableTimeModelSerialization(serializers.ModelSerializer):
    class Meta:
        model=models.AvailableTime
        fields="__all__"

class ReviewModelSerialization(serializers.ModelSerializer):
    class Meta:
        model=models.Review
        fields="__all__"

        