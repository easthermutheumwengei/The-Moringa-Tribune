# Generated by Django 3.2.6 on 2021-09-01 09:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210831_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
