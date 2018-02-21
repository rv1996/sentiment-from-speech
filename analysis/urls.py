from django.urls import path
from .views import sentence

app_name = 'analysis'
urlpatterns = [
    path('', sentence),
]
