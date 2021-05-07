from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    description = RichTextField(verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
        ordering = ['-created']

    def __str__(self):
        return 'درباره ما'
