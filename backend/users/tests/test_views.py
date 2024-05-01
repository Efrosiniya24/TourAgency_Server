import datetime
from unittest import TestCase

from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.response import Response
import jwt

from backend.users.models import User

class SignUpTestCase(APITestCase):
    def test_user_registration(self):
        url = reverse('signUp')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'name': 'Test',
            'phone': '1234567890',
            'surname': 'TestSurname',
            'patronymic': 'TestPatronymic'
        }
        response = self.client.post(url, data, format='json')
        self.assertTrue('id' in response.data)
        self.assertTrue('email' in response.data)
        self.assertEqual(response.data['email'], data['email'])


class SignInTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='teest@example.com',
            password='teestpassword',
            name='Teest',
            phone='11234567890',
            surname='TeestSurname',
            patronymic='TeestPatronymic'
        )
        self.signin_url = reverse('signIn')

    def test_user_signin(self):
        # Создаем тестового пользователя
        user = get_user_model().objects.create(
            email='teest@example.com',
            password='teestpassword',
            name='Teest',
            phone='11234567890',
            surname='TeestSurname',
            patronymic='TeestPatronymic'
        )

        # Отправляем POST запрос для входа пользователя
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(self.signin_url, data, format='json')

        # Проверяем успешный ли был вход (HTTP статус код 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем наличие токена в ответе
        self.assertIn('jwt', response.data)

        # Декодируем токен для проверки содержимого
        token = response.data['jwt']
        decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])

        # Проверяем корректность данных в токене
        self.assertEqual(decoded_token['id'], user.id)
        self.assertTrue('exp' in decoded_token)
        self.assertTrue('iat' in decoded_token)
        exp_time = datetime.datetime.fromtimestamp(decoded_token['exp'])
        self.assertTrue(exp_time > timezone.now())
