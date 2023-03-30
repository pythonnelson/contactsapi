from django.shortcuts import render
from rest_framework.generics import GenericAPIView

class RegistrationView(GenericAPIView):
    def post(self, res):
        pass