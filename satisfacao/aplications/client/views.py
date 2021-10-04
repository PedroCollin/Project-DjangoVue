from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ClientSerializer
from .models import Client

from django.core.exceptions import PermissionDenied


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Apenas o criador pode editar um cliente.')
        
        serializer.save()