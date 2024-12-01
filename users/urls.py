from django.urls import path
from .views import login_view, signup_view, add_address_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('add_address/', add_address_view, name='add_address'),
]
