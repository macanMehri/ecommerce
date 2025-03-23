from django.urls import path, include
from .views import chat_page, error_page, messages_received


urlpatterns = [
    path('message/', chat_page, name='chat_page'),
    path('error/', error_page, name='error_page'),
    path('messages_received/', messages_received, name='messages_received'),
]
