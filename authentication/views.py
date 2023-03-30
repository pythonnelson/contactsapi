from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, resquest):
        #Instantiate the UserSerializer
        serializer=UserSerializer(data=resquest.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


        