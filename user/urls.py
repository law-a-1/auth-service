from django.urls import include, path
from .views import RegisterView,LogoutView, LoginView, UserView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view())
]