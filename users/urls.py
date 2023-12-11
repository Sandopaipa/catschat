from django.urls import path, include
from .views import CreateUserView
import rest_framework.urls
import rest_framework.templates

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='user_create'),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]