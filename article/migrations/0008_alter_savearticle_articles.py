# Generated by Django 3.2 on 2021-05-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_savearticle_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savearticle',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, related_name='save_article', to='article.Article', verbose_name='مقالات'),
        ),
    ]
