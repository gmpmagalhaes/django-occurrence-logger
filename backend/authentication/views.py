from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import SignupSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        return Response({
            'success': True,
            'status_code': status_code,
            'message': 'Successfully registered'
        }, status=status_code)