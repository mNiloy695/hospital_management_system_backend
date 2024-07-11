from django.shortcuts import render
from .models import ContactUs
from .serializers import ContactusSerializer
from rest_framework import viewsets
# Create your views here.
class ContactusViewset(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactusSerializer
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """