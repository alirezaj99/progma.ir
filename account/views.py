from django.shortcuts import render, redirect
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    if request.GET.get("next"):
        return redirect(request.GET.get("next"))
    else:
        return redirect('/')
