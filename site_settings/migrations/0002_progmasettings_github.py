# Generated by Django 3.2 on 2021-05-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progmasettings',
            name='github',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='آیدی گیت هاب'),
        ),
    ]
