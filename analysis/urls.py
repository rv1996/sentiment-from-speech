from django.urls import path
from .views import sentence, AudioView
# from django.conf.urls import static

app_name = 'analysis'
urlpatterns = [
    path('', sentence),
    path('file/',AudioView.as_view()),
]

