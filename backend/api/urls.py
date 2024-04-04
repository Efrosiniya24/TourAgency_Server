from django.contrib import admin
from django.urls import path

from backend.api import views
from backend.api.views import MainPage

urlpatterns = [
    path('', MainPage.as_view()),
]
