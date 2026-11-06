from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserModelTests(TestCase):
    def test_create_user_successful(self):
        email = "businessowner@example.com"
        password = "SecurePassword123!"
        full_name = "Abdullahi Yahaya"
        user = User.objects.create_user(email=email, password=password, full_name=full_name)

        self.assertEqual(user.email, email)
        self.assertEqual(user.full_name, full_name)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertIsNotNone(user.id)

    def test_create_user_without_email_raises_value_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="SecurePassword123!", full_name="No Email User")

    def test_create_superuser_successful(self):
        email = "admin@example.com"
        password = "AdminPassword123!"
        full_name = "System Administrator"
        admin_user = User.objects.create_superuser(email=email, password=password, full_name=full_name)

        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)

    def test_user_str_representation(self):
        user = User(email="test@example.com", full_name="Test Owner")
        self.assertEqual(str(user), "Test Owner (test@example.com)")
