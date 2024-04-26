from django.urls import path, include
from .views import SignUp, SignIn, UserView, LogoutView

urlpatterns = [
    path('signIn', SignIn.as_view()),
    path('signUpp', SignUp.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]
