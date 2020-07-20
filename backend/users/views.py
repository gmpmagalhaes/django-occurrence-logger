from rest_framework import permissions, viewsets, response, status
from .models import CustomUser as User
from .serializers import UserSerializer

class CustomPermission(permissions.BasePermission):
    '''
    If is admin -> allow all (GET, PUT, POST, DELETE)
    If user is owner -> allow RETRIEVE, PATCH
    '''
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        else:
            return True
    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'partial_update']:
            print(request)
            return obj == request.user or request.user.is_staff
        else:
            return request.user.is_staff

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (CustomPermission,)
