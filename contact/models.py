from django.db import models
from django.shortcuts import reverse


class Contact(models.Model):
    name = models.CharField(max_length=130, verbose_name='نام')
    email = models.EmailField(max_length=130, verbose_name='ایمیل')
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')
    time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارتباط")
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس های با ما"
        ordering = ['-time']

    def get_absolute_url(self):
        return reverse('contact:create_contact')
