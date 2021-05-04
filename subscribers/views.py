from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Subscribe
from .forms import SubscribeForm


class SubscribeCreate(CreateView):
    template_name = 'subscribers/subscribe-form.html'
    model = Subscribe
    success_url = reverse_lazy('article:article_list')
    form_class = SubscribeForm
