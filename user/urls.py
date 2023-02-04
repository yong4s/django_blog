from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings

from . import views
from .views import *


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register/', views.register_user, name="register")
    ]

