# Generated by Django 3.2 on 2021-05-07 23:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات'),
        ),
    ]
