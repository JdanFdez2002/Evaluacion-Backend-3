from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static
from foro import views as foro_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('foro/', include('foro.urls', namespace='foro')),
    path('contacto/', include('contacto.urls', namespace='contacto')),
    path('feed/', include('feed.urls', namespace='feed')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('<path:path>', views.custom_404_catchall)]

handler404 = 'core.views.custom_404'
