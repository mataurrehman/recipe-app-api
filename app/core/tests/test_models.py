from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test user created with email successfully """

        email = "test@gmail.com"
        password = "test"
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def create_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GmaIl.com'
        password = 'test'
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a user with no email raises error"""
        password = 'test'
        with self.assertRaisesMessage(ValueError, 'Email is required'):
            get_user_model().objects.create_user(None, password)

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects\
            .create_superuser('test@gmail.com', 'test')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
