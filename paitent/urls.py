from django.urls import path,include 
from .views import activate
from rest_framework.routers import DefaultRouter
from .views import PaitentSerializerView,UserRegistrationViewSet,LoginViewSet,UserLogoutViewSet
router=DefaultRouter()
router.register("paitent",PaitentSerializerView)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',UserRegistrationViewSet.as_view(),name='register'),
    path('active/<uid64>/<token>/',activate,name='activate'),
    path('login/',LoginViewSet.as_view(),name='login'),
    path('logout/',UserLogoutViewSet.as_view(),name='logout'),
]
