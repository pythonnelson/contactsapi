from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Define fields 
    password=serializers.CharField(max_length=65, min_length=9,write_only=True)
    email=serializers.EmailField(max_length=255,min_length=5)
    first_name=serializers.CharField(max_length=255,min_length=2)
    last_name=serializers.CharField(max_length=255,min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    # Override default validation
    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email already in use.')})
        return super().validate(attrs)
    
    # Create a new user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
