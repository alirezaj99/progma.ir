from django.db import models
import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-پروگما{ext}"
    return f"setting/site_logo/{final_name}"


def upload_icon_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-پروگما{ext}"
    return f"setting/site_icon/{final_name}"


class ProgmaSettings(models.Model):
    short_about_us = models.TextField(verbose_name='متن کوتاه درباره ما برای سایدبار',
                                      default='متن کوتاه درباره ما برای سایدبار')
    instagram = models.CharField(max_length=120, verbose_name='آیدی اینستاگرام', default='', blank=True)
    twitter = models.CharField(max_length=120, verbose_name='آیدی توییتر', default='', blank=True)
    telegram = models.CharField(max_length=120, verbose_name='آیدی تلگرام', default='', blank=True)
    youtube = models.CharField(max_length=120, verbose_name='آیدی یوتیوب', default='', blank=True)
    github = models.CharField(max_length=120, verbose_name='آیدی گیت هاب', default='', blank=True)
    site_logo = models.ImageField(upload_to=upload_image_path, verbose_name='لوگوسایت')
    site_icon = models.ImageField(upload_to=upload_icon_image_path,
                                  verbose_name='آیکون سایت در هدر')

    def __str__(self):
        return 'تنظیمات سایت پروگما'

    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'
        ordering = ['-id']
