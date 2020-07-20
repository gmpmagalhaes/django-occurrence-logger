from django.contrib.gis.db import models
from users.models import CustomUser as User

class Occurrence(models.Model):
    CON = 'CONSTRUCTION'
    SPE = 'SPECIAL_EVENT'
    INC = 'INCIDENT'
    WCD = 'WEATHER_CONDITION'
    RCD = 'ROAD_CONDITION'
    CATEGORY_CHOICES=[
        (CON, 'Construction'),
        (SPE, 'Special Event'),
        (INC, 'Incident'),
        (WCD, 'Weather Condition'),
        (RCD, 'Road Condition')
    ]
    category = models.CharField(max_length=17, choices=CATEGORY_CHOICES)

    description = models.TextField(null=False, blank=False)
    TBV = 'TO_BE_VALIDATED'
    VAL = 'VALIDATED'
    RES = 'RESOLVED'
    STATE_CHOICES = [
        (TBV, 'To be validated'),
        (VAL, 'Validated'),
        (RES, 'Resolved')
    ]
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default=TBV)

    location = models.PointField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.category, self.location)
