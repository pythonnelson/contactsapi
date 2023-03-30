from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from . models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


class ContactListView(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Override get_queryset
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    

class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)

    lookup_field = "id"

    # Override get_queryset
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)   
