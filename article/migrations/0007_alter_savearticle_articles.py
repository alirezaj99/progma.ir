# Generated by Django 3.2 on 2021-05-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_savearticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savearticle',
            name='articles',
            field=models.ManyToManyField(blank=True, related_name='save_article', to='article.Article', verbose_name='مقالات'),
        ),
    ]
