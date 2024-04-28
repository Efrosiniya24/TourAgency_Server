from django.urls import path, include
from .views import SignUp, SignIn, UserView, LogoutView, AllUsersView, SearchUserView

urlpatterns = [
    path('signIn', SignIn.as_view()),
    path('signUp', SignUp.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('allUsers', AllUsersView.as_view()),
    path('searchUser', SearchUserView.as_view()),
]
