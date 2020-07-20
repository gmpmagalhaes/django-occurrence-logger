from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import OccurrenceSerializer, UpdateOccurrenceSerializer
from .models import Occurrence
from .filters import OccurrenceFilter

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated or request.user.is_staff
    def has_object_permission(self, request, view, obj):
        return view.action in ['retrieve', 'partial_update', 'destroy'] and request.user == obj or request.user.is_staff

class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = (CustomPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OccurrenceFilter

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT':
            serializer_class = UpdateOccurrenceSerializer
        return serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)