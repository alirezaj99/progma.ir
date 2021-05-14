from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.mixins import UserPassesTestMixin


class Login(LoginView):
    redirect_authenticated_user = reverse_lazy('article:article_list')
    form_class = LoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('article:article_list')
        else:
            return reverse_lazy('article:article_list')

    def form_valid(self, form):
        messages.success(self.request, 'با موفقیت وارد شدی', 'success')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'یه مشکلی هست ، ببین ارور چی میگه ! ( اعتبار سنجی یادت نره )', 'danger')
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدی', 'success')
    if request.GET.get("next"):
        return redirect(request.GET.get("next"))
    else:
        return redirect('/')


class Register(UserPassesTestMixin, CreateView):
    model = User
    success_url = reverse_lazy('account:login')
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    permission_denied_message = "You are already registered!"

    def test_func(self):
        return self.request.user.is_anonymous

    def form_valid(self, form):
        messages.success(self.request, 'با موفقیت ثبت نام شدی', 'success')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'یه مشکلی هست ، ببین ارور چی میگه ! ( اعتبار سنجی یادت نره )', 'danger')
        return super().form_invalid(form)
