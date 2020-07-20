from rest_framework import routers
from .views import OccurrenceViewSet

router = routers.DefaultRouter()

router.register('occurrences', OccurrenceViewSet)