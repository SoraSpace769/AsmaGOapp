from django.contrib import admin
from users import views
from django.urls import path

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('admin/', admin.site.urls),
]
