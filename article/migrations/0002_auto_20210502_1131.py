# Generated by Django 3.2 on 2021-05-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='عنوان برچسب')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='آدرس برچسب')),
                ('active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='آدرس مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=400, verbose_name='عنوان مقاله'),
        ),
    ]