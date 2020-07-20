import django_filters
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D, Distance
from django.contrib.gis.geos import GEOSGeometry
from .utils import getCoordsFromAddress
from .models import Occurrence

class OccurrenceFilter(django_filters.FilterSet):
    point = django_filters.CharFilter(label='point', method='filter_by_distance')
    local = django_filters.CharFilter(label='location', method='filter_by_distance')
    radius = django_filters.NumberFilter(label='distance', method='filter_by_distance')
    ADR = 'ADDRESS'
    COR = 'COORDINATES'
    LOCATION_TYPE_CHOICES = (
        [ADR, 'Address'],
        [COR, 'Coordinates']
    )
    location_type = django_filters.ChoiceFilter(choices=LOCATION_TYPE_CHOICES, label="location type", method="filter_by_distance")

    class Meta:
        model = Occurrence
        fields = ('category', 'user',)

    def filter_by_distance(self, queryset, name, value):
        point = self.request.query_params.get('point').split(',') or [0, 0]
        local = self.request.query_params.get('local') or None
        filter_dist = self.request.query_params.get('radius') or 10
        location_type = self.request.query_params.get('location_type') or 'COORDINATES'
        if local:
            pnt = GEOSGeometry(getCoordsFromAddress(self, local), srid=4326)
        else:
            pnt = GEOSGeometry('POINT(' + str(point[0]) + ' ' + str(point[1]) +')', srid=4326)
        queryset = queryset.filter(location__distance_lte=(pnt, D(km=float(filter_dist))))
        return queryset