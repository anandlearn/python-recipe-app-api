from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test Creating a new user with an email is successful
        :return:
        """
        email = "test@123.com"
        password = 'password'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for new user is normalized.
        :return:
        """
        email = "test@ABC.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test Creating user with no email raised error
        :return:
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test!@3')

    def test_create_new_super_user(self):
        """
        Test creating a new super user
        :return:
        """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
