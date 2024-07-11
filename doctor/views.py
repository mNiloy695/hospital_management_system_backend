from django.shortcuts import render
from  rest_framework import viewsets
from rest_framework.pagination  import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Doctor,Specialization,Designation,AvailableTime,Review
# Create your views here.
from .serializers import DoctorModelSerializer,SpecializatinModelSerializer,DesignationModelSerializer,AvailableTimeModelSerialization,ReviewModelSerialization
from rest_framework import filters
class DoctorPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
class DoctorViewsets(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    pagination_class=DoctorPagination
    serializer_class=DoctorModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ["user__first_name","user__last_name","user__email","user__id"]


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=SpecializatinModelSerializer


class DesignationViewSet(viewsets.ModelViewSet):
    queryset=Designation.objects.all()
    serializer_class=DesignationModelSerializer


# time filter for specific doctor

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        doctor_id=request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset


class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset=AvailableTime.objects.all()
    serializer_class=AvailableTimeModelSerialization
    filter_backends=[AvailableTimeForSpecificDoctor]

class ReviewForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset
class ReviewViewSet(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewModelSerialization
    filter_backends=[ReviewForSpecificDoctor]
    