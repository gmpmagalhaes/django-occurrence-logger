from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser

class CustomUserModelTest(TestCase):

    def create_user(self):
        return CustomUser.objects.create(username='user', email='email@email.com', password='password', is_staff=False, is_active=True, date_joined=timezone.now)

    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, CustomUser))