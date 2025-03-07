from django.urls import path
from .views import ContactFormAPI

urlpatterns = [
    path('form', ContactFormAPI.as_view(), name='contact_form'),
]