from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_change, name='detect_change'),
]
