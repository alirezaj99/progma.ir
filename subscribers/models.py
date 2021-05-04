from django.db import models
from django.db.models.signals import post_save


class SubscribeManager(models.Manager):
    def get_active_subscribe(self):
        return self.get_queryset().filter(active=True)


class Subscribe(models.Model):
    email = models.EmailField(max_length=60, unique=True, verbose_name='ایمیل')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = "مشترک"
        verbose_name_plural = "مشترک ها"
        ordering = ['-created']

    def __str__(self):
        return self.email
