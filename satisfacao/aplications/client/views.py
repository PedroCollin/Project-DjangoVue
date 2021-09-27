from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ClientSerializer
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)