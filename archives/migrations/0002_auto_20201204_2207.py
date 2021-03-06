# Generated by Django 3.0.5 on 2020-12-04 22:07

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('archives', '0001_initial'),
        ('taggit', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infobase',
            name='genres',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='articles.TaggedGenres', to='taggit.GenreTag', verbose_name='теги'),
        ),
        migrations.AddField(
            model_name='infobase',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='articles.TaggedWhatever', to='taggit.CustomTag', verbose_name='жанри'),
        ),
    ]
