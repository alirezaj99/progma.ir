from django.db import models
from django.utils import timezone
from account.models import User
import os
import random
from ckeditor.fields import RichTextField
from django.db.models import Q
from extensions.utils import jalali_converter
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
from subscribers.models import Subscribe


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_list_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.slug}{ext}"
    return f"articles/image-list/{final_name}"


def upload_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.slug}{ext}"
    return f"articles/image/{final_name}"


class ArticleManager(models.Manager):
    def get_publish_article(self):
        return self.get_queryset().filter(status='p')

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(tags__title__icontains=query)
                  )
        return self.get_queryset().filter(lookup, status='p').distinct()


class ArticleTagManager(models.Manager):
    def get_active_tag(self):
        return self.get_queryset().filter(active=True)


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آی پی آدرس")
    time = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت")

    class Meta:
        verbose_name = "آی پی آدرس"
        verbose_name_plural = "آی پی آدرس ها"

    def __str__(self):
        return self.ip_address

    def jtime(self):
        return jalali_converter(self.time)

    jtime.short_description = "زمان ثبت"


class ArticleTag(models.Model):
    title = models.CharField(max_length=400, verbose_name="عنوان برچسب")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس برچسب")
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ArticleTagManager()

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب"
        ordering = ['-created']

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.active:
    #         for article in self.article_tags.get_publish_article():
    #             article.status = 'd'
    #             article.save()
    #     super(ArticleTag, self).save(*args, **kwargs)


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),  # draft
        ('p', "منتشر شده"),  # publish
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=400, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس مقاله")
    description = RichTextField(verbose_name="محتوا")
    image_list = models.ImageField(upload_to=upload_image_list_path, verbose_name="تصویر 135*135 مقاله")
    image = models.ImageField(upload_to=upload_image_path, verbose_name="تصویر مقاله")
    tags = models.ManyToManyField(ArticleTag, blank=True, related_name='article_tags', verbose_name='تگ ها / برچسب ها')
    hits = models.ManyToManyField(IPAddress, blank=True, related_name="article_hits", verbose_name="بازید")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")

    objects = ArticleManager()

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def author_str(self):
        return str(self.author)

    author_str.short_description = 'نویسنده'

    def tags_str(self):
        return " - ".join([tag.title for tag in self.tags.get_active_tag()])

    tags_str.short_description = 'تگ ها / برچسب ها'


class SaveArticle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='save_article', verbose_name='کاربر')
    articles = models.ManyToManyField(Article, related_name='save_article', verbose_name='مقالات', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مقاله ذخیره شده"
        verbose_name_plural = "مقالات ذخیره شده"
        ordering = ['-created']

    def __str__(self):
        return str(self.user)

    def get_articles(self):
        return self.articles


def send_email_users(sender, instance, created, **kwargs):
    emails = []
    for sub in Subscribe.objects.get_active_subscribe():
        emails += sub.email.split()
    if created and instance.status == 'p':
        subject = 'welcome to progma'
        message = f'Hi , thank you for registering in {instance.title}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = emails
        send_mail(subject, message, email_from, recipient_list)
    while instance.status == 'p':
        subject = 'welcome to progma'
        message = f'Hi , thank you for registering in {instance.title}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = emails
        send_mail(subject, message, email_from, recipient_list)
        break


post_save.connect(send_email_users, sender=Article)
