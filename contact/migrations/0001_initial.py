# Generated by Django 3.2 on 2021-05-09 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='نام', max_length=130, verbose_name='نام')),
                ('email', models.EmailField(default='test@test.com', max_length=130, verbose_name='ایمیل')),
                ('subject', models.CharField(default='موضوع', max_length=300, verbose_name='موضوع')),
                ('message', models.TextField(default='متن پیام', verbose_name='متن پیام')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارتباط')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس های با ما',
                'ordering': ['-time'],
            },
        ),
    ]