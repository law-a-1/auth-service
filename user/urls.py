from django.urls import include, path
from .views import RegisterView,LogoutView, LoginView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view())
]