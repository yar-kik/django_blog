# Generated by Django 3.0.5 on 2020-09-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_users_bookmark'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['slug'], name='articles_ar_slug_452037_idx'),
        ),
    ]