from django.urls import path
from .views import SubscribeCreate

app_name = 'subscribers'

urlpatterns = [
    path('subscribe/', SubscribeCreate.as_view(), name='subscribe'),
]
