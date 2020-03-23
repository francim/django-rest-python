from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test create a new user with email successful """
        email = "pippo@gmail.com"
        password = "plotone"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        """Test email normalized"""
        email = "pluto@GMAIL.COM"
        user = get_user_model().objects.create_user(email=email, password="test1234")

        self.assertEqual(user.email,email.lower())

    def test_create_user_email_wrong(self):
        """Test creating user with wrong email raises Error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,password="test123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(email="t@super.com",
                                                         password="test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
