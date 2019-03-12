from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloView.as_view(), name='hello'),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='register'),
]
