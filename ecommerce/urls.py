from django.contrib import admin
from django.urls import path, include
from .local_settings import ADMIN_PATH
from online_shop.views import index_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(f'{ADMIN_PATH}', admin.site.urls),
    path('', index_view, name='index'),
    path('users/', include('users.urls')),
    path('online_shop/', include('online_shop.urls')),
    path('chat/', include('chat.urls')),
    path('charts/', include('charts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
