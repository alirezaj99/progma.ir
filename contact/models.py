from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=130, verbose_name='نام', default='نام')
    email = models.EmailField(max_length=130, verbose_name='ایمیل', default='test@test.com')
    subject = models.CharField(max_length=300, verbose_name='موضوع', default='موضوع')
    message = models.TextField(verbose_name='متن پیام', default='متن پیام')
    time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارتباط")
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس های با ما"
        ordering = ['-time']


