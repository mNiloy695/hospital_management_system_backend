from django.urls  import path,include
from .views import AppointmentViewSet

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('',AppointmentViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
