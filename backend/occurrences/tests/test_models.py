from django.test import TestCase
from django.utils import timezone
from occurrences.models import Occurrence
from users.models import CustomUser

class OccurrenceModelTest(TestCase):

    def create_occurrence(self):
        user = CustomUser.objects.create(username='user', email='email@email.com', password='password')
        return Occurrence.objects.create(category='CONSTRUCTION', description='A simple test', location='POINT(55 22)', user=user, state='TO_BE_VALIDATED', created_at=timezone.now, updated_at=timezone.now)

    def test_occurrence_creation(self):

        occur = self.create_occurrence()
        self.assertTrue(isinstance(occur, Occurrence))