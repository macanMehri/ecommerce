from django.contrib import admin
from django.urls import path, include
from .local_settings import ADMIN_PATH

urlpatterns = [
    path(f'{ADMIN_PATH}', admin.site.urls),
    path('users/', include('users.urls')),
    path('online_shop/', include('online_shop.urls'))
]
