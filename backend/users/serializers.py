from rest_framework import serializers
from .models import CustomUser as User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('date_joined', 'last_login', )
        extra_kwargs= { 'password': {'write_only': True}, 'first_name': {'write_only': True}, 'last_name': { 'write_only': True}}
