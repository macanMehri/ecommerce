from django.urls import path
from .views import login_view, signup_view, add_address_view, get_cities, my_addresses_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('add_address/', add_address_view, name='add_address'),
    path('get_cities/<int:province_id>/', get_cities, name='get_cities'),
    path('my_addresses/', my_addresses_view, name='my_addresses'),
]
