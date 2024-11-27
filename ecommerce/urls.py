from django.contrib import admin
from django.urls import path, include
from .local_settings import ADMIN_PATH
from online_shop.views import index_view
urlpatterns = [
    path(f'{ADMIN_PATH}', admin.site.urls),
    path('', index_view, name='index'),
    path('users/', include('users.urls')),
    path('online_shop/', include('online_shop.urls'))
]
