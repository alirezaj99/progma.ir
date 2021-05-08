from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    about = AboutUs.objects.first()
    context = {'about_us': about}
    return render(request, 'about_us/about-us.html', context)
