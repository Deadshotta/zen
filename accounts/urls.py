# accounts/urls.py

from django.urls import path
from .views import signup, login_view, home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),  # Home page after login
]
