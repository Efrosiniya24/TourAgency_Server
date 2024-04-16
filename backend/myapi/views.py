from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'mainPage.html'


class Login(TemplateView):
    template_name = "login.html"


class SignUp(TemplateView):
    template_name = "registration.html"


class AboutUs(TemplateView):
    template_name = 'aboutUs.html'


class MainAdmin(TemplateView):
    template_name = 'mainAdmin.html'
