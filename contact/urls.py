from django.urls import path
from .views import CreateContact

app_name = 'contact'

urlpatterns = [
    path('contact/', CreateContact.as_view(), name='create_contact'),
]
