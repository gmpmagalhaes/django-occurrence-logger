from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #('username','email', 'date_joined', 'last_login', 'password')
        read_only_fields = ('date_joined', 'last_login',)
        extra_kwargs= { 'password': {'write_only': True}, 'first_name': {'write_only': True}, 'last_name': { 'write_only': True}}
