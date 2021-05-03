# Generated by Django 3.2 on 2021-05-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آی پی آدرس')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')),
            ],
            options={
                'verbose_name': 'آی پی آدرس',
                'verbose_name_plural': 'آی پی آدرس ها',
            },
        ),
    ]
