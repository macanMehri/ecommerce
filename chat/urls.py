from django.urls import path, include
from .views import chat_page, messages_received, create_connection


urlpatterns = [
    path('message/', chat_page, name='chat_page'),
    path('messages_received/', messages_received, name='messages_received'),
    path('create_connection/<int:user_id>', create_connection, name='create_connection'),
]
