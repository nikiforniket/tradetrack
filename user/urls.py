# -*- coding: utf-8 -*-

from django.urls import path

from user.views import LoginView, LogOutView


user_paths = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout")
]
