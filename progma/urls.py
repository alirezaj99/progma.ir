from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from account.views import logout_view
from about_us.views import about_us
from decouple import config

urlpatterns = [
    path('', include("article.urls", namespace="article")),
    path('', include('social_django.urls', namespace='social')),
    path('', include('subscribers.urls', namespace='subscribers')),
    path('', include('contact.urls', namespace='contact')),
    path('about-us/', about_us, name='about_us'),
    path('logout/', logout_view, name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # ADD ROOT STATIC FILES
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # ADD MEDIA STATIC FILES
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
