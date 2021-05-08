from django.shortcuts import render
from site_settings.models import ProgmaSettings


def site_sidebar(request):
    settings = ProgmaSettings.objects.first()
    context = {
        'settings': settings
    }
    return render(request, 'Shared/Sidebar.html', context)


def site_header_references(request):
    settings = ProgmaSettings.objects.first()
    context = {
        'settings': settings
    }
    return render(request, 'Shared/__HeaderReferences.html', context)
