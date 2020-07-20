from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import CustomUser as User
class SignupSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(max_length=18)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)
        extra_kwargs = { 'password': { 'write_only': True}, 'password_confirmation': { 'write_only': True}}
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirmation'):
            raise serializers.ValidationError('Passwords do not match')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'])
        return user