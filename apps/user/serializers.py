from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(UserCreateSerializer):
    def validate_password(self, value):
        # Evitar la validación de contraseña
        return value
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', "img_profile",'first_name', 'phone', 'dni', 'last_name','expected_entry_time', 'expected_exit_time','is_active', 'is_staff')







