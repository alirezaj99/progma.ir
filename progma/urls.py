from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from account.views import logout_view
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include("article.urls", namespace="article")),
    path('', include('social_django.urls', namespace='social')),
    path('', include('subscribers.urls', namespace='subscribers')),
    path('', include('contact.urls', namespace='contact')),
    path('', include('about_us.urls', namespace='about_us')),
    path('', include('account.urls', namespace='account')),
    path('logout/', logout_view, name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/login/', RedirectView.as_view(url='/')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    path('admin/', admin.site.urls),
]

handler404 = 'progma.views.view_404'
handler403 = 'progma.views.view_403'
handler400 = 'progma.views.view_400'
handler500 = 'progma.views.view_500'

if settings.DEBUG:
    # ADD ROOT STATIC FILES
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # ADD MEDIA STATIC FILES
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
