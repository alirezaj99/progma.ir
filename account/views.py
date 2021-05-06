from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages


def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدی', 'success')
    if request.GET.get("next"):
        return redirect(request.GET.get("next"))
    else:
        return redirect('/')
