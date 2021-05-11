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


# ERRORS

def view_404(request, exception):
    context = {

    }
    return render(request, "errors/404.html", context)


def view_403(request, exception):
    context = {

    }
    return render(request, "errors/403.html", context)


def view_400(request, exception):
    context = {

    }
    return render(request, "errors/400.html", context)


def view_500(request):
    context = {

    }
    return render(request, "errors/500.html", context)
