from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'mainPage.html'


class Login(TemplateView):
    template_name = "login.html"
