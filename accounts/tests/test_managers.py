from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normaluser@email.com', password='foo')
        self.assertEqual(user.email, 'normaluser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            #check if username is None for AbstractUser 
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@mail.com', password='foo')
        self.assertEqual(admin_user.email, 'super@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            #check if username for superuser is None for AbstractUser 
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email = 'super@user.com', password='foo', is_superuser=False
            )

