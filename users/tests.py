from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse


class TestUserCreateView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_user_url = reverse('user_create')
        self.login_url = reverse('rest_framework:login')
        self.logout_url = reverse('rest_framework:logout')
        self.data = {
            'username': 'Rulon',
            'password': 'StRoNg123456'
        }

    def test_user_create_view(self):
        """
        Тестирование регистрации пользвоателя.
        """
        response = self.client.post(
            path=self.create_user_url, data=self.data, format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_user_login_view(self):
        """
        Тестирование входа пользователя в аккаунт.
        """
        request = self.client.post(
            path=self.login_url, data=self.data, format='json'
        )
        self.assertEqual(
            request.status_code, 200
        )

    def test_user_logout_view(self):
        """
        Тестирование выхода пользователя из аккаунта
        """
        request = self.client.post(
            path=self.logout_url
        )
        self.assertEqual(
            request.status_code, 200
        )