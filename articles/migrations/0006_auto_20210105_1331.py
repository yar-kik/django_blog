# Generated by Django 3.0.5 on 2021-01-05 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201226_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date_created',), 'permissions': [('can_moderate_article', 'Може одобрювати статті'), ('can_draft_article', 'Може створювати чернетку статті')]},
        ),
        migrations.RemoveField(
            model_name='article',
            name='medium_picture',
        ),
        migrations.RemoveField(
            model_name='article',
            name='small_picture',
        ),
    ]
