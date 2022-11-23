from django.urls import path 
from .views import *
urlpatterns = [
    path("subscription", CreateSubscription.as_view()),
    path("webhook", webhook.as_view())
]