from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from progma import settings
from account.views import logout_view

urlpatterns = [
    path('', include("article.urls", namespace="article")),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # ADD ROOT STATIC FILES
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # ADD MEDIA STATIC FILES
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
