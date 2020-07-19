from rest_framework import serializers
from rest_framework_simplejwt import serializers
from django_contrib.auth.models import User

class SignupSerializer(serializers.Models):

    password_confirmation = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')
        extra_kwargs = { 'password_confirmation': { 'write_only': True}}
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirmation'):
            raise serializers.ValidationError('Passwords do not match')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user

class LoginJWTSerializer(serializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get('password')
        }
        user = User.objects.filter(email=attrs.get('identifier')).first() or User.objects.filter(username=attrs.get('identifier')).first()
        if user:
            credentials['username']: user.username
        return super().validated_data(credentials)