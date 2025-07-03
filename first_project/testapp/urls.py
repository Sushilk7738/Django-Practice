from django.contrib import admin
from django.urls import path, include
from testapp import views


urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.welcome, name="welcome"),

]