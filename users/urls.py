from django.urls import path
from .views import (
    login_view, signup_view, add_address_view, get_cities, user_dash_view, delete_address,
    change_username, change_password, change_email
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('add_address/', add_address_view, name='add_address'),
    path('get_cities/<int:province_id>/', get_cities, name='get_cities'),
    path('dashboard/', user_dash_view, name='dashboard'),
    path('change_username/', change_username, name='change_username'),
    path('change_password/', change_password, name='change_password'),
    path('change_email/', change_email, name='change_email'),
    path('confirm_address_delete/<int:user_address_id>', delete_address, name='confirm_address_delete')
]
