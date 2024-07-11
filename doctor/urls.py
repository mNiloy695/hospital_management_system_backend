from django.urls import path,include
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewsets,ReviewViewSet,SpecializationViewSet,DesignationViewSet,AvailableTimeViewset
router=DefaultRouter()
router.register('list',DoctorViewsets)
router.register('review',ReviewViewSet)
router.register('specialization',SpecializationViewSet)
router.register('designation',DesignationViewSet)
router.register('time',AvailableTimeViewset)

urlpatterns = [
    path('',include(router.urls)),
]
