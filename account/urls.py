from django.urls import path
from .views import Login,Register

app_name = 'account'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
]
