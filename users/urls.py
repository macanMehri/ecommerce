from django.urls import path
from .views import login_view, signup_view, get_cities_by_province, add_address_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path(
        'get_cities_by_province/<int:province_id>/',
        get_cities_by_province,
        name='get_cities_by_province'),
    path('add_address/', add_address_view, name='add_address'),
]
