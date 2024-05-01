from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.views import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SignIn(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': timezone.now() + timezone.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()

        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt': token}
        return response



class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success',
        }
        return response


class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class SearchUserView(APIView):
    def get(self, request):
        # Получаем параметры запроса из URL
        query_params = request.query_params

        # Извлекаем значения полей Имя, Фамилия и Отчество из запроса
        name = query_params.get('name')
        last_name = query_params.get('last_name')
        patronymic = query_params.get('patronymic')

        # Создаем словарь для хранения фильтров
        filters = {}

        # Добавляем фильтры для существующих значений
        if name:
            filters['name__icontains'] = name
        if last_name:
            filters['last_name__icontains'] = last_name
        if patronymic:
            filters['patronymic__icontains'] = patronymic

        # Поиск пользователей в базе данных
        users = User.objects.filter(**filters)

        # Сериализация найденных пользователей
        serializer = UserSerializer(users, many=True)

        # Возвращаем данные пользователей в формате JSON
        return Response(serializer.data)
