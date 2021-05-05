from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Subscribe
from .forms import SubscribeForm
from django.contrib import messages


class SubscribeCreate(CreateView):
    template_name = 'subscribers/subscribe-form.html'
    model = Subscribe
    success_url = reverse_lazy('article:article_list')
    form_class = SubscribeForm

    def form_valid(self, form):
        messages.success(self.request, 'همه چیز به خوبی انجام شد ، منتظر مقالات باش', 'success')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'یه مشکلی هست ، ببین ارور چی میگه !', 'danger')
        return super().form_invalid(form)
