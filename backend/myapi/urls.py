from django.contrib import admin
from django.urls import path

from backend.myapi import views
from backend.myapi.views import MainPage, Login, SignUp, AboutUs, MainAdmin

urlpatterns = [
    path('', MainPage.as_view()),
    path('login/', Login.as_view()),
    path('signUp/', SignUp.as_view()),
    path('aboutUs/', AboutUs.as_view()),
    path('mainAdmin/', MainAdmin.as_view()),
]
