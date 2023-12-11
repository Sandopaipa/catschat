from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cat


class TestCatListView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('cat_list_create')
        self.data = {
            "catname": "adminCat"
        }
        self.user = User.objects.create_user(username='Rulon', password='StRoNg123456')

        self.client.force_login(self.user)

    def test_cats_list_create_view(self):
        """
        Тестирование получения списка питомцев и добавления новых.
        """
        response = self.client.get(
            path=self.url
        )

        self.assertEqual(
            response.status_code, 200
        )
        request = self.client.post(
            path=self.url, data=self.data, format='json'
        )
        self.assertEqual(
            request.status_code, 201
        )


class TestCatViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.cat = Cat.objects.create(catname='usercat1', owner=self.user)

        self.client.force_login(self.user)

        self.update_url = f'/cats/{self.cat.pk}/update/'
        self.delete_url = f'/cats/{self.cat.pk}/delete/'

        self.cat_new_data = {
            "cat_birthdate": "2001-01-01",
            'breed': 'RUSSIAN_BLUE',
            'fur': 'LONG'
        }

    def test_cats_detail_view(self):
        """
        Тестирование получения данных о созданном питомце.
        """
        response = self.client.get(f'/cats/{self.cat.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_cats_update_view(self):
        """
        Тестирование обоновления данных питомца.
        """
        request = self.client.patch(
            path=self.update_url, data=self.cat_new_data, content_type='application/json'
        )
        self.assertEqual(
            request.status_code, 200
        )

    def test_cats_delete_view(self):
        """
        Тестирование удаления питомца из списка.
        """
        request = self.client.delete(
            path=self.delete_url
        )
        self.assertEqual(
            request.status_code, 204
        )
